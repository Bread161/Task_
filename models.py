
from django.db import models
from django.contrib.auth.models import User
# tasks/models.py
STATUS_CHOICES = (
    ('queued', 'В очереди'),
    ('in_progress', 'В процессе'),
    ('completed', 'Завершена')
)
# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='queued')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


