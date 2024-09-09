from typing import List, Any
from db.models import SensorDataModel
import pandas as pd

class AllSensorData:
    hours: str
    data: List[dict[str, Any]]

def convert_query_to_json(rows: List[SensorDataModel]):
    data = [
        {
            'id': item.id,
            'equipmentId': item.equipment_id,
            'value': float(item.value),
            'timestamp': item.timestamp.isoformat()
        }
        for item in rows
    ]

    return data

def calculate_average_sensor_data(data: list[dict[str, Any]], round = 2) -> List[dict[str, Any]]:
    df = pd.DataFrame(data)

    average_value_per_sensor = df.groupby('equipmentId')['value'].mean().reset_index()
    average_value_per_sensor['value'] = average_value_per_sensor['value'].round(round)

    return average_value_per_sensor.to_dict(orient='records')

def format_data(data: List[SensorDataModel]):
    json_results = convert_query_to_json(data)
    average_values = calculate_average_sensor_data(json_results)

    return average_values
