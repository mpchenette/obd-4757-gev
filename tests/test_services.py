import pytest
from flask import Flask
from models import db, Task
from services import TaskService

@pytest.fixture
def app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    return app

@pytest.fixture
def test_db(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()
        yield db
        db.session.remove()
        db.drop_all()

@pytest.fixture
def task_service(test_db):
    return TaskService()

def test_create_task(task_service, app):
    with app.app_context():
        task_data = {
            'title': 'New Task',
            'description': 'Test Description',
            'status': 'pending',
            'priority': 3
        }
        task = task_service.create_task(task_data)
        assert task.title == task_data['title']
        assert task.description == task_data['description']
        assert task.status == task_data['status']
        assert task.priority == task_data['priority']

def test_get_all_tasks(task_service, app):
    with app.app_context():
        # Create some test tasks
        task_service.create_task({'title': 'Task 1'})
        task_service.create_task({'title': 'Task 2'})
        
        tasks = task_service.get_all_tasks()
        assert len(tasks) == 2
        assert tasks[0].title == 'Task 1'
        assert tasks[1].title == 'Task 2'

def test_get_tasks_by_status(task_service, app):
    with app.app_context():
        task_service.create_task({'title': 'Task 1', 'status': 'pending'})
        task_service.create_task({'title': 'Task 2', 'status': 'completed'})
        
        pending_tasks = task_service.get_tasks_by_status('pending')
        completed_tasks = task_service.get_tasks_by_status('completed')
        
        assert len(pending_tasks) == 1
        assert len(completed_tasks) == 1
        assert pending_tasks[0].status == 'pending'
        assert completed_tasks[0].status == 'completed'

def test_update_task(task_service, app):
    with app.app_context():
        task = task_service.create_task({'title': 'Original Title'})
        
        updated = task_service.update_task(task.id, {
            'title': 'Updated Title',
            'status': 'completed'
        })
        
        assert updated.title == 'Updated Title'
        assert updated.status == 'completed'
        
        # Test updating non-existent task
        assert task_service.update_task(999, {'title': 'Test'}) is None

def test_delete_task(task_service, app):
    with app.app_context():
        task = task_service.create_task({'title': 'To Delete'})
        
        # Test successful deletion
        assert task_service.delete_task(task.id) is True
        assert task_service.get_task_by_id(task.id) is None
        
        # Test deleting non-existent task
        assert task_service.delete_task(999) is False