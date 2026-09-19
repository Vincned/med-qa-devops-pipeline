import pytest
import requests

BASE_URL = "hhtp://app:8000"

@pytest.fixture(scope="session")
def api_client():
    #Session fixture for run the HHTP-requests
    session = requests.Session()
    session.headers.update({"Content-Type": "application/json"})
    yield session
    session.close()

@pytest.fixture
def sample_patient():
    #Fixture with generation of valid patient data
    return {
        "patient_id": "P-100",
        "age": 30,
        "status": "active"
    }