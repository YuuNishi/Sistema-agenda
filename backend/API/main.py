from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class Patient(BaseModel):
    id: int = None
    name: str = None
class Appointment(BaseModel):
    id: int = None
    doctor_id: int = None
    hour: datetime = None

patients_list = []
appointments_list = []
@app.post("/patient")
async def create_patient(patient: Patient):
    patients_list.append(patient)
    return patient
@app.get("/patient")
async def get_patient():
    return patients_list
@app.post("/appointment")
async def create_patient(appointment: Appointment):
    appointments_list.append(appointment)
    return appointments_list
@app.get("/appointment/{id}")
async def get_appointment(id: int):
    result = list(filter(lambda x: x.id == id, appointments_list))
    return result[0]

@app.get("/")
async def root():
    return {"message": "Olá, mundo!!!!"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
