from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(title="Patient Management API")

class Patient(BaseModel):
    patient_id: str
    age: int
    status: str

patients_db = {}

@app.get("/health")
def healthcheck():
    return {"status": "ok"}

@app.post("/patient", status_code=status.HTTP_201_CREATED)
def create_patient(patient: Patient):
    if patient.age < 0 or patient.age > 120:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid age"
        )
    patients_db[patient.patient_id] = patient
    return {"message": "Patient created", "patient": patient}