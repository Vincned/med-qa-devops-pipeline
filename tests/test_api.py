import pytest

BASE_URL = "http://app:8000"

def test_healthcheck(api_client):
    #Endpoint available check /health
    response = api_client.get(f"{BASE_URL}/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_create_patient_success(api_client, sample_patient):
    #Patient success creation
    response = api_client.post(f"{BASE_URL}/patient", json=sample_patient)
    assert response.status_code == 201
    assert response.json()["message"] == "Patient created"
    assert response.json()["patient"]["patient_id"] == sample_patient["patient_id"]

@pytest.mark.parametrize("invalid_age", [-1, 150])
def test_create_patient_invalid_age(api_client, invalid_age):
    #Age validation check (negative scenarios)
    payLoad = {
        "patient_id": "P-ERR",
        "age": invalid_age,
        "status": "acitve"
    }
    response = api_client.post(f"{BASE_URL}/patient", json=payLoad)
    assert response.status_code == 400
    assert response.json()["detail"] == "Invalid age"