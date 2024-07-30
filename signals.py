
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Task
from .search_indexes import TaskIndex

@receiver(post_save, sender=Task)
def index_post(sender, instance, **kwargs):
    task_doc = TaskIndex(meta={'id': instance.id}, title=instance.title, description=instance.description)
    task_doc.save()
