# Celery worker
from celery import Celery
app = Celery('tasks', broker='redis://localhost:6379/0')
@app.task
def test_task():
    return 'Task Completed'