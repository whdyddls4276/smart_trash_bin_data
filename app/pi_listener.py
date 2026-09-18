import firebase_admin
from firebase_admin import credentials, firestore

# Firebase 인증 및 초기화
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# UID 저장용 전역 변수
current_uid = None

# Firestore에서 UID가 변경될 때마다 호출되는 함수
def on_uid_change(doc_snapshot, changes, read_time):
    global current_uid
    for doc in doc_snapshot:
        current_uid = doc.to_dict().get("uid")
        print(f"✅ UID 업데이트됨: {current_uid}")

# Firestore 리스너 등록
doc_ref = db.collection("current_uid").document("latest")
doc_ref.on_snapshot(on_uid_change)

# 프로그램 계속 실행 유지
print("🟢 UID 리스너 실행 중...")
import time
while True:
    time.sleep(1)