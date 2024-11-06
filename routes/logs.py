# routes/logs.py
from flask import Blueprint, render_template, request
from models import SimulationData, Predictions
from datetime import datetime, timedelta

logs_bp = Blueprint('logs', __name__)


@logs_bp.route('/logs', methods=['GET', 'POST'])
def logs():
    # 기본 날짜를 오늘로 설정하고, 선택된 날짜가 있으면 해당 날짜 사용
    selected_date = request.form.get("date", datetime.now().strftime('%Y-%m-%d'))

    # 시작 및 종료 날짜를 설정 (선택된 날짜의 하루 동안의 데이터)
    start_date = datetime.strptime(selected_date, '%Y-%m-%d')
    end_date = start_date + timedelta(days=1)  # 다음 날 자정 전까지를 포함

    simulation_data = SimulationData.query.filter(
        SimulationData.observation_time >= start_date,
        SimulationData.observation_time < end_date
    ).all()

    predictions_data = Predictions.query.filter(
        Predictions.observation_time >= start_date,
        Predictions.observation_time < end_date
    ).all()

    return render_template('logs.html',
                           simulation_data=simulation_data,
                           predictions_data=predictions_data,
                           selected_date=selected_date)
