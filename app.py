from flask import Flask, render_template, jsonify, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from db_config import db, SQLALCHEMY_DATABASE_URI
from models import RealTimeData, ForecastData
from user import get_user_by_username, users

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SESSION_COOKIE_SECURE'] = False  # 개발 환경에서는 False
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'
db.init_app(app)

# Flask-Login 설정
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    # 'users' 딕셔너리에서 ID로 사용자 객체를 반환
    return users.get(user_id)

# 로그인 페이지
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = get_user_by_username(username)

        if user and user.verify_password(password):
            login_user(user)
            next_page = request.args.get('next')
            # next_page가 로그인 페이지 또는 None인 경우 대시보드로 리다이렉트
            if not next_page or next_page.startswith('/login'):
                next_page = url_for('home')
            return redirect(next_page)
        else:
            flash('Invalid username or password', 'danger')

    return render_template('login.html')

# 로그아웃 페이지
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

# 대시보드 페이지
@app.route('/')
@login_required
def home():
    print(f"Current user: {current_user}")  # 디버깅용 출력
    return render_template('index.html')

# 실시간 데이터 API
@app.route('/api/real-time-data', methods=['GET'])
@login_required
def get_real_time_data():
    start_date = request.args.get('start_date')  # YYYY-MM-DD 형식
    end_date = request.args.get('end_date')      # YYYY-MM-DD 형식

    query = RealTimeData.query
    if start_date:
        query = query.filter(RealTimeData.timestamp >= start_date)
    if end_date:
        query = query.filter(RealTimeData.timestamp <= end_date)

    data = query.order_by(RealTimeData.timestamp.desc()).all()
    return jsonify([item.to_dict() for item in data])

# 예측 데이터 API
@app.route('/api/forecast-data', methods=['GET'])
@login_required
def get_forecast_data():
    start_date = request.args.get('start_date')  # YYYY-MM-DD 형식
    end_date = request.args.get('end_date')      # YYYY-MM-DD 형식

    query = ForecastData.query
    if start_date:
        query = query.filter(ForecastData.fcstDateTime >= start_date)
    if end_date:
        query = query.filter(ForecastData.fcstDateTime <= end_date)

    data = query.order_by(ForecastData.fcstDateTime.desc()).all()
    return jsonify([item.to_dict() for item in data])

# 로그 페이지
@app.route('/logs', methods=['GET'])
@login_required
def logs():
    date = request.args.get('date')  # YYYY-MM-DD 형식
    data_type = request.args.get('type')  # 'generation' 또는 'forecast'

    data = []

    # 발전량 데이터 조회
    if data_type == 'generation':
        query = RealTimeData.query
        if date:
            query = query.filter(RealTimeData.timestamp.like(f"{date}%"))
        data = query.order_by(RealTimeData.timestamp.desc()).all()

    # 예측량 데이터 조회
    elif data_type == 'forecast':
        query = ForecastData.query
        if date:
            query = query.filter(ForecastData.fcstDateTime.like(f"{date}%"))
        data = query.order_by(ForecastData.fcstDateTime.desc()).all()

    # 데이터 변환
    formatted_logs = []
    for item in data:
        if isinstance(item, RealTimeData):
            formatted_logs.append({
                "timestamp": item.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
                "generation": item.generation,
                "charging": item.charging,
                "discharging": item.discharging,
                "reactive_power": item.reactive_power,
                "power_factor": item.power_factor,
                "frequency": item.frequency,
                "rs_voltage": item.rs_voltage,
                "ss_voltage": item.ss_voltage
            })
        elif isinstance(item, ForecastData):
            formatted_logs.append({
                "powergen": item.powergen,
                "cum_powergen": item.cum_powergen,
                "irrad": item.irrad,
                "temp": item.temp,
                "wind": item.wind
            })

    return render_template('logs.html', logs=formatted_logs, date=date, data_type=data_type)



if __name__ == '__main__':
    app.run(debug=True)
