# quickstart/services.py
from django_socio_grpc import generics

from .models import Tasks
from .serializers import TasksProtoSerializer

from django_filters.rest_framework import DjangoFilterBackend


# This service will have only the List and Create actions
class TasksService(generics.AsyncListCreateService):
    queryset = Tasks.objects.all()
    serializer_class = TasksProtoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["status"]
