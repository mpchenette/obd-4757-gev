# obd-4757-gev

A simple Flask-based Task Management API for demonstrating GitHub Copilot features. This project implements a RESTful API for managing tasks with CRUD operations.

## Features

- CRUD operations for tasks
- Filter tasks by status
- Task prioritization
- Proper separation of concerns
- RESTful API design

## Project Structure

- `app.py` - Main Flask application with API routes
- `models.py` - Database models for tasks
- `services.py` - Business logic layer for task operations
- `requirements.txt` - Project dependencies

## Setup and Installation

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Run the application:
   ```
   python app.py
   ```

3. API will be available at `http://localhost:5000`

## API Endpoints

- `GET /tasks` - Get all tasks or filter by status
- `GET /tasks/<id>` - Get a specific task by ID
- `POST /tasks` - Create a new task
- `PUT /tasks/<id>` - Update an existing task
- `DELETE /tasks/<id>` - Delete a task

## API Usage Examples

### Create a new task
```
POST /tasks
Content-Type: application/json

{
  "title": "Complete project",
  "description": "Finish the demo project",
  "priority": 3,
  "status": "pending"
}
```

### Update task status
```
PUT /tasks/1
Content-Type: application/json

{
  "status": "completed"
}
```

## Demo
---
1. Unit Test Generation
   - /tests
   - Copilot Edits
2. Commenting / Documentation
   - Edits to add comments / docstrings
   - Create README
        - tell copilot to also add a desciption section, section on how to run and potential future improvements section
3. Other Copilot Features
   - Code Review(s)
   - Vision? arch diagram to terraform?
4. Custom Instructions
   - show using to specify unit test framework
5. Agent mode?
   - run this for me? self-healing? python envs? ask it to add a gui interface?