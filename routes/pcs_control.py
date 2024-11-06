# routes/pcs_control.py
from flask import Blueprint, render_template

pcs_control_bp = Blueprint('pcs_control', __name__)

@pcs_control_bp.route('/')
def pcs_control():
    return render_template('pcs_control.html')
