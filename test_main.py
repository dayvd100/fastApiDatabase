from fastapi.testclient import TestClient
from .database import TestingSessionLocal, Base, TestingEngine
from .main import app

Base.metadata.create_all(bind=TestingEngine)

client = TestClient(app)


def test_example():
    with TestingSessionLocal():
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == {"message": "this is crazy"}
