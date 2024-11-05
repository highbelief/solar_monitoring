# routes/logs.py
from flask import Blueprint, render_template, request
from models import SimulationData, Predictions
from datetime import datetime

logs_bp = Blueprint('logs', __name__)


@logs_bp.route('/logs', methods=['GET', 'POST'])
def logs():
    # 기본 날짜를 오늘로 설정
    selected_date = request.form.get("date", datetime.now().strftime('%Y-%m-%d'))

    # 선택한 날짜의 데이터를 필터링하여 조회
    start_date = datetime.strptime(selected_date, '%Y-%m-%d')
    end_date = start_date.replace(hour=23, minute=59, second=59)

    simulation_data = SimulationData.query.filter(
        SimulationData.observation_time >= start_date,
        SimulationData.observation_time <= end_date
    ).all()

    predictions_data = Predictions.query.filter(
        Predictions.observation_time >= start_date,
        Predictions.observation_time <= end_date
    ).all()

    return render_template('logs.html',
                           simulation_data=simulation_data,
                           predictions_data=predictions_data,
                           selected_date=selected_date)
