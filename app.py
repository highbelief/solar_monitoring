# app.py
from flask import Flask, redirect, url_for  # redirect와 url_for을 추가로 임포트
from config import Config
from models import db
from routes import init_app  # 블루프린트 초기화 함수 가져오기

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

# 블루프린트 초기화
init_app(app)

# 기본 경로 리디렉션 설정 (대시보드 페이지로 이동)
@app.route('/')
def index():
    return redirect(url_for('dashboard.dashboard'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # 데이터베이스 테이블 생성 (필요 시)
    app.run(debug=True)