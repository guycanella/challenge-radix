from sqlalchemy import Column, Integer, String, Numeric, TIMESTAMP, text
from app.db.base import Base

class SensorDataModel(Base):
    __tablename__ = 'data_sensor'
    id = Column('id', Integer, primary_key=True, nullable=False, autoincrement=True)
    equipament_id = Column('equipament_id', String(100  ), nullable=False, unique=True)
    value = Column('value', Numeric, nullable=False)
    timestamp = Column('timestamp', TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'))