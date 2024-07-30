from .tasks import process_task
from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from elasticsearch_dsl import Q
from .search_indexes import TaskIndex
# Create your views here.

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        task = serializer.save(user=self.request.user)
        process_task.delay(task.id)

    @action(detail=False, methods=['get'])
    def all_tasks(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def search(self, request):
        query = request.GET.get('q')
        q = Q('multi_match', query=query, fields=['title', 'description'])
        search = TaskIndex.search().query(q)
        response = search.execute()
        results = [hit.to_dict() for hit in response]
        return Response(results
