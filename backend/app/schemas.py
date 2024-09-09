from pydantic import BaseModel, field_validator
from typing import Optional, List
from datetime import datetime
import pandas as pd
import re

class SensorDataPayload(BaseModel):
    equipmentId: str
    value: float
    timestamp: Optional[datetime] = None

    @field_validator('equipmentId')
    def check_equipment_id(cls, equip_id: str):
        if not re.match('^EQ-(1248[6-9]|1249[0-5])$', equip_id):
            raise ValueError('Equipment ID not allowed.')
        return equip_id

    @field_validator('value')
    def check_value(cls, value: float):
        if pd.isna(value):
            raise ValueError('Empty value in a row')

        if value < 0.0 or value > 90.0:
            raise ValueError('Value of measure not allowed.')

        return value

class SensorDataItem(BaseModel):
    equipmentId: str
    value: float

class SensorDataResponse(BaseModel):
    data: List[SensorDataItem]