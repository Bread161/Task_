
from celery import shared_task
from .models import Task
import time

@shared_task
def process_task(task_id):
    task = Task.objects.get(id=task_id)
    task.status = 'in_progress'
    task.save()
    time.sleep(10)  # Симуляция обработки задачи
    task.status = 'completed'
    task.save()
