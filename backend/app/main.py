from fastapi import FastAPI
from routes.get_data_sensor import router as get_data_sensor_router
from routes.insert_json import router as insert_data_sensor
from routes.insert_csv import router as insert_data_sensor_csv

app = FastAPI()

@app.get("/")
def home():
    return { "message": "Hello, World" }

app.include_router(get_data_sensor_router)
app.include_router(insert_data_sensor)
app.include_router(insert_data_sensor_csv)
