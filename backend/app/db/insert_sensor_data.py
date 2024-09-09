from datetime import date
from decouple import config
import psycopg2
import csv
import os

filename = 'data_sensor.dat'

if not os.path.exists(filename):
    raise FileNotFoundError(f'File {filename} not found.')

if os.path.getsize(filename) == 0:
    raise ValueError(f'File {filename} is empty')

connection = psycopg2.connect(
    host=config('DB_HOST'),
    port=config('PORT'),
    dbname=config('POSTGRES_DB'),
    user=config('POSTGRES_USER'),
    password=config('POSTGRES_PASSWORD')
)

cursor = connection.cursor()

def insert_data(equipment_id: str, value: float, timestamp: date) -> None:
    query = f"""
    INSERT INTO {config('TABLE_NAME')} (equipment_id, value, timestamp)
    VALUES (%s, %s, %s)
    """
    cursor.execute(query, (equipment_id, value, timestamp))

with open(filename, 'r') as file:
    reader = csv.reader(file)

    for row in reader:
        equipment_id, value, timestamp = row
        insert_data(equipment_id, value, timestamp)

connection.commit()
cursor.close()
connection.close()