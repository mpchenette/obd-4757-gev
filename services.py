from models import db, Task

class TaskService:
    
    def get_all_tasks(self):
        return Task.query.all()
    
    def get_tasks_by_status(self, status):
        return Task.query.filter_by(status=status).all()
    
    def get_task_by_id(self, task_id):
        return Task.query.get(task_id)
    
    def create_task(self, task_data):
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
        task = self.get_task_by_id(task_id)
        if not task:
            return False
        
        db.session.delete(task)
        db.session.commit()
        return True