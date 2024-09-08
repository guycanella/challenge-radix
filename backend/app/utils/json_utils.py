from typing import List, Any
from db.models import SensorDataModel
import pandas as pd

def convert_query_to_json(rows: List[SensorDataModel]):
    data = [
        {
            'id': item.id,
            'equipamentId': item.equipament_id,
            'value': float(item.value),
            'timestamp': item.timestamp.isoformat()
        }
        for item in rows
    ]

    return data

def calculate_average_sensor_data(data: list[dict[str, Any]], round = 2):
    df = pd.DataFrame(data)

    average_value_per_sensor = df.groupby('equipamentId')['value'].mean().reset_index()
    average_value_per_sensor['value'] = average_value_per_sensor['value'].round(round)

    return average_value_per_sensor.to_dict(orient='records')