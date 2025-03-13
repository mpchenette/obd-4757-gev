import pytest
from datetime import datetime
from models import Task, db

def test_new_task():
    """Test Task model creation"""
    task = Task(
        title="Test Task",
        description="Test Description",
        status="pending",
        priority=3
    )
    
    assert task.title == "Test Task"
    assert task.description == "Test Description"
    assert task.status == "pending"
    assert task.priority == 3
    assert isinstance(task.created_at, datetime)
    assert isinstance(task.updated_at, datetime)

def test_task_to_dict():
    """Test Task model to_dict method"""
    task = Task(
        title="Test Task",
        description="Test Description",
        status="pending",
        priority=3
    )
    
    task_dict = task.to_dict()
    assert isinstance(task_dict, dict)
    assert task_dict['title'] == "Test Task"
    assert task_dict['description'] == "Test Description"
    assert task_dict['status'] == "pending"
    assert task_dict['priority'] == 3
    assert 'created_at' in task_dict
    assert 'updated_at' in task_dict

def test_task_repr():
    """Test Task model string representation"""
    task = Task(id=1, title="Test Task")
    assert str(task) == '<Task 1: Test Task>'