from django_socio_grpc import proto_serializers
from rest_framework import serializers
from .models import Tasks
from tasks.grpc.tasks_pb2 import (
    TasksListResponse,
    TasksResponse,
)


class TaskPayloadSerializer(serializers.Serializer):
    email = serializers.EmailField()
    subject = serializers.CharField()
    body = serializers.CharField()


class TasksProtoSerializer(proto_serializers.ModelProtoSerializer):
    data = TaskPayloadSerializer(many=False)
    status = serializers.ReadOnlyField()

    class Meta:
        model = Tasks
        fields = "__all__"

        proto_class = TasksResponse
        proto_class_list = TasksListResponse
