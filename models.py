from db_config import db

class RealTimeData(db.Model):
    __tablename__ = 'real_time_data'
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, nullable=False, unique=True)
    generation = db.Column(db.Float)
    charging = db.Column(db.Float)
    discharging = db.Column(db.Float)
    reactive_power = db.Column(db.Float)
    power_factor = db.Column(db.Float)
    frequency = db.Column(db.Float)
    rs_voltage = db.Column(db.Float)
    ss_voltage = db.Column(db.Float)

    def to_dict(self):
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}

class ForecastData(db.Model):
    __tablename__ = 'forecast_data'
    id = db.Column(db.Integer, primary_key=True)
    fcstDateTime = db.Column(db.DateTime, nullable=False, unique=True)
    powergen = db.Column(db.Float, nullable=False)
    cum_powergen = db.Column(db.Float)
    irrad = db.Column(db.Float)
    temp = db.Column(db.Float)
    wind = db.Column(db.Float)

    def to_dict(self):
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}
