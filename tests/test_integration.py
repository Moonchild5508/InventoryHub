import pytest
from backend import app

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

def test_get_inventory(client):
    response = client.get('/inventory')
    assert response.status_code == 200
    assert 'data' in response.json

def test_add_inventory(client):
    response = client.post('/inventory', json={"name": "Test Item", "quantity": 10})
    assert response.status_code == 200
    assert response.json['status'] == 'success'
