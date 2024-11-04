# config.py
class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://solar_user:password@localhost/SolarDB'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'your_secret_key'  # 필요한 경우, 보안을 위해 사용
