from flask import Flask, request
from flask_cors import CORS  # ✅ 추가

app = Flask(__name__)
CORS(app)  # ✅ 전체 앱에 CORS 허용

current_uid = None

@app.route('/set_uid', methods=['POST'])
def set_uid():
    global current_uid
    data = request.json
    current_uid = data.get('uid')
    print(f"✅ UID 설정됨: {current_uid}")
    return {'status': 'success', 'received_uid': current_uid}