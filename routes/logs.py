# routes/logs.py
from flask import Blueprint, render_template
from models import SimulationData, Predictions

logs_bp = Blueprint('logs', __name__)

@logs_bp.route('/logs')
def logs():
    # 데이터베이스에서 simulation_data와 predictions 데이터를 모두 조회하여 템플릿에 전달
    simulation_data = SimulationData.query.all()
    predictions_data = Predictions.query.all()
    return render_template('logs.html', simulation_data=simulation_data, predictions_data=predictions_data)
