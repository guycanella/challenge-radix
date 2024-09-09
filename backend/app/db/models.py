from sqlalchemy import Column, Integer, String, Numeric, DateTime
import datetime
from .base import Base

class SensorDataModel(Base):
    __tablename__ = 'data_sensor'
    id = Column('id', Integer, primary_key=True, nullable=False, autoincrement=True)
    equipment_id = Column('equipment_id', String(100), nullable=False)
    value = Column('value', Numeric, nullable=False)
    timestamp = Column('timestamp', DateTime, default=datetime.datetime.now())