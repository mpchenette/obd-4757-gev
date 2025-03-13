from flask import Flask, request, jsonify, render_template
from models import Task, db
from services import TaskService

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database with the app
db.init_app(app)

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

task_service = TaskService()

# Root route to serve the HTML interface
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/tasks', methods=['GET'])
def get_tasks():
    status = request.args.get('status')
    if status:
        tasks = task_service.get_tasks_by_status(status)
    else:
        tasks = task_service.get_all_tasks()
    
    return jsonify([task.to_dict() for task in tasks])

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = task_service.get_task_by_id(task_id)
    if task:
        return jsonify(task.to_dict())
    return jsonify({'error': 'Task not found'}), 404

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    if not data or 'title' not in data:
        return jsonify({'error': 'Title is required'}), 400
    
    task = task_service.create_task(data)
    return jsonify(task.to_dict()), 201

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    task = task_service.update_task(task_id, data)
    
    if task:
        return jsonify(task.to_dict())
    return jsonify({'error': 'Task not found'}), 404

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    result = task_service.delete_task(task_id)
    if result:
        return jsonify({'message': 'Task deleted successfully'})
    return jsonify({'error': 'Task not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)