# routes/__init__.py
from flask import Blueprint
from .dashboard import dashboard_bp
from .logs import logs_bp
from .user_management import user_management_bp
from .pcs_control import pcs_control_bp

def init_app(app):
    app.register_blueprint(dashboard_bp, url_prefix='/dashboard')
    app.register_blueprint(logs_bp, url_prefix='/logs')
    app.register_blueprint(user_management_bp, url_prefix='/user_management')
    app.register_blueprint(pcs_control_bp, url_prefix='/pcs_control')