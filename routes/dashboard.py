from flask import Blueprint, render_template, jsonify
from models import SimulationData, Predictions
from datetime import datetime, timedelta

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/')  # URL을 /dashboard로 매핑
def dashboard():
    # 다음 날의 날짜를 계산
    tomorrow = datetime.now().date() + timedelta(days=1)

    # 다음 날 데이터만 가져옴
    predictions_data = Predictions.query.filter(
        Predictions.observation_time >= datetime.combine(tomorrow, datetime.min.time()),
        Predictions.observation_time < datetime.combine(tomorrow, datetime.max.time())
    ).all()

    return render_template('dashboard.html', predictions_data=predictions_data)

# routes/dashboard.py
@dashboard_bp.route('/api/current_power')
def current_power():
    current_data = SimulationData.query.order_by(SimulationData.observation_time.desc()).limit(10).all()
    current_data_list = [{'time': data.observation_time.strftime('%Y-%m-%d %H:%M:%S'), 'value': data.power_generated} for data in current_data]
    return jsonify(current_data_list)
