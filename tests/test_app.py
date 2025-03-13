import pytest
import json
from app import app as flask_app
from models import db

@pytest.fixture
def app():
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    flask_app.config['TESTING'] = True
    return flask_app

@pytest.fixture
def client(app):
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client
            db.session.remove()
            db.drop_all()

def test_index_route(client):
    """Test the main page loads"""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Task Manager' in response.data

def test_create_task_api(client):
    """Test task creation endpoint"""
    task_data = {
        'title': 'API Test Task',
        'description': 'Created via API',
        'priority': 4
    }
    response = client.post('/tasks',
                         data=json.dumps(task_data),
                         content_type='application/json')
    assert response.status_code == 201
    data = json.loads(response.data)
    assert data['title'] == task_data['title']
    assert data['description'] == task_data['description']
    assert data['priority'] == task_data['priority']

def test_get_tasks_api(client):
    """Test getting all tasks endpoint"""
    # Create some test tasks first
    task_data = [
        {'title': 'Task 1', 'status': 'pending'},
        {'title': 'Task 2', 'status': 'completed'}
    ]
    for task in task_data:
        client.post('/tasks',
                   data=json.dumps(task),
                   content_type='application/json')
    
    # Test getting all tasks
    response = client.get('/tasks')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert len(data) == 2
    
    # Test filtering by status
    response = client.get('/tasks?status=pending')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert len(data) == 1
    assert data[0]['status'] == 'pending'

def test_update_task_api(client):
    """Test task update endpoint"""
    # Create a task first
    task = client.post('/tasks',
                      data=json.dumps({'title': 'Original Task'}),
                      content_type='application/json')
    task_id = json.loads(task.data)['id']
    
    # Update the task
    update_data = {
        'title': 'Updated Task',
        'status': 'completed'
    }
    response = client.put(f'/tasks/{task_id}',
                         data=json.dumps(update_data),
                         content_type='application/json')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['title'] == update_data['title']
    assert data['status'] == update_data['status']
    
    # Test updating non-existent task
    response = client.put('/tasks/999',
                         data=json.dumps(update_data),
                         content_type='application/json')
    assert response.status_code == 404

def test_delete_task_api(client):
    """Test task deletion endpoint"""
    # Create a task first
    task = client.post('/tasks',
                      data=json.dumps({'title': 'Task to Delete'}),
                      content_type='application/json')
    task_id = json.loads(task.data)['id']
    
    # Delete the task
    response = client.delete(f'/tasks/{task_id}')
    assert response.status_code == 200
    
    # Verify task is deleted
    response = client.get(f'/tasks/{task_id}')
    assert response.status_code == 404
    
    # Test deleting non-existent task
    response = client.delete('/tasks/999')
    assert response.status_code == 404