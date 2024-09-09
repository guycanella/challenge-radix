from fastapi import APIRouter, UploadFile, File, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session
from db.connection import get_db
from db.models import SensorDataModel
from io import StringIO
from schemas import SensorDataPayload
import pandas as pd

router = APIRouter()

@router.post('/data-sensor/csv')
async def insert_data_sensor_csv(file: UploadFile = File(...), db: Session = Depends(get_db)):
    if file.content_type != 'text/csv':
        raise HTTPException(status_code = 400, detail = "Invalid file type. Please upload a CSV file.")

    try:
        contents = await file.read()
        df = pd.read_csv(StringIO(contents.decode('utf-8')))

        if not {'equipmentId', 'value', 'timestamp'}.issubset(df.columns):
            raise HTTPException(status_code = 400, detail = "CSV file must contain columns: equipmentId, value, timestamp.")

        rows = df.to_dict(orient = 'records')

        for row in rows:
            validated_data = SensorDataPayload(
                equipmentId = row['equipmentId'],
                value = row['value'],
                timestamp = pd.to_datetime(row['timestamp']) if 'timestamp' in row else None
            )

            data = SensorDataModel(
                equipment_id = validated_data.equipmentId,
                value = validated_data.value,
                timestamp = validated_data.timestamp
            )

            db.add(data)

        db.commit()

        return Response(status_code = status.HTTP_201_CREATED)

    except Exception as error:
        db.rollback()
        raise HTTPException(status_code = 500, detail = str(error))

    finally:
        await file.close()