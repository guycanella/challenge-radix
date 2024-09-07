from typing import List
from db.models import SensorDataModel

def convert_query_to_json(rows: List[SensorDataModel]):
    data = [
        {
            'id': item.id,
            'equipamentId': item.equipament_id,
            'value': item.value,
            'timestamp': item.timestamp.isoformat()
        }
        for item in rows
    ]

    return data