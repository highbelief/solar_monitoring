# routes/__init__.py
from flask import Blueprint

# 각 블루프린트를 임포트하고 이름을 지정합니다.
from .dashboard import dashboard_bp
from .logs import logs_bp

def init_app(app):
    # 블루프린트를 Flask 앱에 등록합니다.
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(logs_bp)
