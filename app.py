from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB 설정
client = MongoClient('mongodb+srv://test:123123123@cluster0.bdulsxi.mongodb.net/?retryWrites=true&w=majority')
db = client['mydatabase']

@app.route('/')
def index():
    # MongoDB에서 모든 usernames를 조회
    user_list = db['usernames'].find({})
    # 조회된 사용자 이름을 리스트에 추가
    usernames = [{'username': user['username']} for user in user_list]
    # index.html에 usernames 리스트 전달
    return render_template('index.html', usernames=usernames)

@app.route('/submit', methods=['POST'])
def submit():
    # request.form을 통해 form 데이터에 접근
    username = request.form['username']
    # MongoDB에 username 저장
    db['usernames'].insert_one({'username': username})
    # 메인 페이지로 리다이렉트
    return jsonify(message=f'Username: {username} saved successfully')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
