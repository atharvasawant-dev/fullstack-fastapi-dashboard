from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)

def test_index_renders():
    r = client.get('/')
    assert r.status_code == 200
    assert 'Developer Dashboard' in r.text

def test_metrics_api():
    r = client.get('/api/metrics')
    assert r.status_code == 200
    payload = r.json()
    assert payload['status'] == 'ok'
