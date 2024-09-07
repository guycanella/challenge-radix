from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session
from db.connection import get_db
from db.models import SensorDataModel
from datetime import datetime
import schemas

router = APIRouter()

@router.post('/data-sensor', status_code=status.HTTP_201_CREATED)
def insert_data_sensor(payload: schemas.SensorDataPayload, db: Session = Depends(get_db)):
    timestamp = payload.timestamp if payload.timestamp else datetime.now()

    new_data = SensorDataModel(
        equipament_id = payload.equipamentId,
        value = payload.value,
        timestamp = timestamp
    )

    db.add(new_data)
    db.commit()
    db.refresh(new_data)

    return Response(status_code=status.HTTP_201_CREATED)