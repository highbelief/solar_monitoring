from flask_sqlalchemy import SQLAlchemy

DATABASE_CONFIG = {
    'USER': 'your_username',
    'PASSWORD': 'your_password',
    'HOST': 'localhost',
    'DB_NAME': 'forecast_db'
}

SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{DATABASE_CONFIG['USER']}:{DATABASE_CONFIG['PASSWORD']}@{DATABASE_CONFIG['HOST']}/{DATABASE_CONFIG['DB_NAME']}"
db = SQLAlchemy()
