import pytest
from app import app as flask_app

@pytest.fixture
def app():
    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()

def test_cowsay(app, client):
    message = 'hello'
    res = client.get('/cowsay/%s/' % message)
    assert res.status_code == 200
    page_output = res.get_data(as_text=True)
    assert message in page_output
    assert "(obo)\___" in page_output

def test_fortune(app, client):
    res = client.get('/fortune/')
    page_output = res.get_data(as_text=True)
    assert "<pre>" in page_output
    assert res.status_code == 200

def test_index(app, client):
    res = client.get('/')
    page_output = res.get_data(as_text=True)
    assert res.status_code == 302

def test_cowfortune(app, client):
    res = client.get('/cowfortune/')
    page_output = res.get_data(as_text=True)
    assert "<pre>" in page_output
    assert "(oo)\____" in page_output
    assert res.status_code == 200

