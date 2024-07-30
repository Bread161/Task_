
from elasticsearch_dsl import Document, Text
from .models import Task

class TaskIndex(Document):
    title = Text()
    description = Text()

    class Index:
        name = 'tasks'

    def save(self, **kwargs):
        return super().save(**kwargs)

def bulk_indexing():
    TaskIndex.init()
    for task in Task.objects.all():
        task_doc = TaskIndex(meta={'id': task.id}, title=task.title, description=task.description)
        task_doc.save()
