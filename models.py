# models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class SimulationData(db.Model):
    __tablename__ = 'simulation_data'
    id = db.Column(db.BigInteger, primary_key=True)
    observation_time = db.Column(db.TIMESTAMP, nullable=False)
    temperature = db.Column(db.Float)
    solar_irradiance = db.Column(db.Float)
    humidity = db.Column(db.Float)
    cloud_coverage = db.Column(db.Float)
    equipment_status = db.Column(db.String(255))
    power_generated = db.Column(db.Float)
    created_at = db.Column(db.TIMESTAMP, default=db.func.current_timestamp())

class Predictions(db.Model):
    __tablename__ = 'predictions'
    id = db.Column(db.BigInteger, primary_key=True)
    observation_time = db.Column(db.TIMESTAMP, nullable=False)
    predicted_power_generated = db.Column(db.Float)
    predicted_battery_level = db.Column(db.Float)
    predicted_equipment_status = db.Column(db.String(255))
    created_at = db.Column(db.TIMESTAMP, default=db.func.current_timestamp())
