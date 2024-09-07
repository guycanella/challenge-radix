from pydantic import BaseModel, field_validator
import re

class SensorData(BaseModel):
    equipament_id: str
    value: float

    @field_validator('equipament_id')
    def check_equipament_id(cls, eqId: str):
        if not re.match('^EQ-(1248[6-9]|1249[0-5])$', eqId):
            raise ValueError('Equipament ID not allowed.')
        return eqId

    @field_validator('value')
    def check_value(cls, value: float):
        if value < 0.0 or value > 90.0:
            raise ValueError('Value of measure nto allowed.')
        return value