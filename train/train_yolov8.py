"""
YOLOv8 학습 스크립트 (Google Colab에서 실행)

데이터셋:
  - 재활용 폐기물 이미지 1,910장, 3클래스(Can / Glass / Plastic)
  - Roboflow에서 라벨링 — 일부를 직접 라벨링해 기준을 만들고, 자동 라벨링으로 나머지를
    확장한 뒤 잘못 붙은 라벨만 수정해 최종 데이터셋 구성 (version 3)

출력:
  - best.pt              : 학습된 가중치
  - best_float32.tflite  : 라즈베리파이 탑재용 변환 파일

실행 전:
  export ROBOFLOW_API_KEY="..."   (Colab이면 os.environ에 직접 설정)
"""

import os

# !pip install -q ultralytics roboflow

from roboflow import Roboflow
from ultralytics import YOLO

# ── 설정 ────────────────────────────────────────────────
API_KEY   = os.environ["ROBOFLOW_API_KEY"]   # 키를 코드에 적지 않는다
WORKSPACE = "yongin"
PROJECT   = "trash-vbwlc"
VERSION   = 3

EPOCHS = 3
IMGSZ  = 416
BATCH  = 8

# ── 1. 데이터셋 다운로드 ──────────────────────────────────
rf = Roboflow(api_key=API_KEY)
project = rf.workspace(WORKSPACE).project(PROJECT)
dataset = project.version(VERSION).download("yolov8")

# ── 2. 학습 ─────────────────────────────────────────────
model = YOLO("yolov8n.pt")
model.train(
    data=dataset.location + "/data.yaml",
    epochs=EPOCHS,
    imgsz=IMGSZ,
    batch=BATCH,
)

# ── 3. 라즈베리파이용 변환 ────────────────────────────────
model.export(format="tflite")

print("학습 완료")
print("  runs/detect/train/weights/best.pt")
print("  runs/detect/train/weights/best_saved_model/best_float32.tflite")
