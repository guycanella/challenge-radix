from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from datetime import date, timedelta
from db.connection import get_db
from db.models import SensorDataModel
from typing import Union
from utils.json_utils import convert_query_to_json, calculate_average_sensor_data

router = APIRouter()

possible_periods = ["24", "48", "168", "720"]

@router.get('/data-sensor')
def get_data_sensor(period: Union[str, None] = None, db: Session = Depends(get_db)):
    if period is None:
        results = db.query(SensorDataModel).all()

        json_results = convert_query_to_json(results)
        average_values = calculate_average_sensor_data(json_results)

        return { "data": average_values }

    if period not in possible_periods:
        raise HTTPException(status_code=404, detail="Period not found.")

    end_date = date.today()
    start_date = end_date - timedelta(hours=float(period))

    results = db.query(SensorDataModel).filter(
        SensorDataModel.timestamp.between(start_date, end_date)
    ).all()

    json_results = convert_query_to_json(results)
    average_values = calculate_average_sensor_data(json_results)

    return { "data": average_values }
