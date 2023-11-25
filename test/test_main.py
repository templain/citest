from starlette.testclient import TestClient
import main

def test_hello_world():
    client = TestClient(main.api)
    response = client.get('/')
    assert response.status_code == 200
    assert response.text == 'Hello, World!'
