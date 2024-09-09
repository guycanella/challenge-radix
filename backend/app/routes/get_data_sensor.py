from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from schemas import SensorDataResponse
from db.connection import get_db
from db.models import SensorDataModel
from typing import Union
from utils.json_utils import format_data

router = APIRouter()

possible_periods = ["24", "48", "168", "720"]

@router.get('/data-sensor', response_model = SensorDataResponse)
def get_data_sensor(period: Union[str, None] = None, db: Session = Depends(get_db)):
    if period is None:
        results = db.query(SensorDataModel).all()

        average_values = format_data(results)

        return SensorDataResponse(data = average_values)

    if period not in possible_periods:
        raise HTTPException(status_code = 404, detail = "Period not found.")

    end_date = datetime.now()
    start_date = end_date - timedelta(hours = float(period))

    results = db.query(SensorDataModel).filter(
        SensorDataModel.timestamp.between(start_date, end_date)
    ).all()

    average_values = format_data(results)

    return SensorDataResponse(data = average_values)
