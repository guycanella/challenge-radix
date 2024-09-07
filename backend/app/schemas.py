from pydantic import BaseModel, field_validator
from typing import Optional
from datetime import datetime
import re

class SensorDataPayload(BaseModel):
    equipamentId: str
    value: float
    timestamp: Optional[datetime] = None

    @field_validator('equipamentId')
    def check_equipament_id(cls, equip_id: str):
        if not re.match('^EQ-(1248[6-9]|1249[0-5])$', equip_id):
            raise ValueError('Equipament ID not allowed.')
        return equip_id

    @field_validator('value')
    def check_value(cls, value: float):
        if value < 0.0 or value > 90.0:
            raise ValueError('Value of measure nto allowed.')
        return value