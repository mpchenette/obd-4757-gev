from models import db, Task

class TaskService:
    """Service class for handling task-related business logic"""
    
    def get_all_tasks(self):
        """
        Get all tasks from the database
        
        Returns:
            list: List of all Task objects
        """
        return Task.query.all()
    
    def get_tasks_by_status(self, status):
        """
        Get tasks filtered by status
        
        Args:
            status (str): The status to filter by
            
        Returns:
            list: List of Task objects with the specified status
        """
        return Task.query.filter_by(status=status).all()
    
    def get_task_by_id(self, task_id):
        """
        Get a specific task by ID
        
        Args:
            task_id (int): The ID of the task to retrieve
            
        Returns:
            Task: The found task or None if not found
        """
        return Task.query.get(task_id)
    
    def create_task(self, task_data):
        """
        Create a new task
        
        Args:
            task_data (dict): Dictionary containing task data
            
        Returns:
            Task: The newly created task
        """
        new_task = Task(
            title=task_data['title'],
            description=task_data.get('description', ''),
            status=task_data.get('status', 'pending'),
            priority=task_data.get('priority', 1)
        )
        
        db.session.add(new_task)
        db.session.commit()
        return new_task
    
    def update_task(self, task_id, task_data):
        """
        Update an existing task
        
        Args:
            task_id (int): ID of the task to update
            task_data (dict): Dictionary containing updated task data
            
        Returns:
            Task: The updated task or None if not found
        """
        task = self.get_task_by_id(task_id)
        if not task:
            return None
        
        if 'title' in task_data:
            task.title = task_data['title']
        if 'description' in task_data:
            task.description = task_data['description']
        if 'status' in task_data:
            task.status = task_data['status']
        if 'priority' in task_data:
            task.priority = task_data['priority']
        
        db.session.commit()
        return task
    
    def delete_task(self, task_id):
        """
        Delete a task
        
        Args:
            task_id (int): ID of the task to delete
            
        Returns:
            bool: True if the task was deleted, False if not found
        """
        task = self.get_task_by_id(task_id)
        if not task:
            return False
        
        db.session.delete(task)
        db.session.commit()
        return True