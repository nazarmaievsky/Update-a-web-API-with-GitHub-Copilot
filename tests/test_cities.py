from fastapi.testclient import TestClient
from app.main import app  # Import your actual app instance

client = TestClient(app)

def test_get_spain_cities():
    response = client.get("/countries/ES/cities")
    assert response.status_code == 200
    assert "Madrid" in response.text