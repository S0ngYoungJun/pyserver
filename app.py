# app.py
from flask import Flask, send_from_directory

app = Flask(__name__)

# 정적 파일 제공을 위한 루트 경로 설정
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)