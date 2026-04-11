import pytest
from main import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_todos(client):
    response = client.get('/api/todos')
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_add_todo(client):
    response = client.post('/api/todos', json={'task': 'Test Task'})
    assert response.status_code == 201
    assert response.json['task'] == 'Test Task'
    assert response.json['completed'] is False

def test_update_todo(client):
    # Update the first todo in the list
    response = client.put('/api/todos/1', json={'completed': True})
    assert response.status_code == 200
    assert response.json['completed'] is True

def test_delete_todo(client):
    # Delete the second todo in the list
    response = client.delete('/api/todos/2')
    assert response.status_code == 200
    
    # Verify it is gone
    get_response = client.get('/api/todos')
    ids = [t['id'] for t in get_response.json]
    assert 2 not in ids
