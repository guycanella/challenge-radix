from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return { "message": "Hello, World" }

@app.get("/data-sensor")
def get_data_sensor():
    return { "message": "Get Data from database." }

@app.post("/data-sensor")
def post_data_sensor():
    return {}

@app.post("/data-sensor-csv")
def post_data_sensor_csv():
    return {}