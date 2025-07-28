import pytest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_app_is_working(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Server is running ..." in response.data
