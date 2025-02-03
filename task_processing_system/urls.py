"""
URL configuration for task_processing_system project.
"""

from django_socio_grpc.services.app_handler_registry import AppHandlerRegistry

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
]


from tasks.services import TasksService


def grpc_handlers(server):
    app_registry = AppHandlerRegistry("tasks", server)
    app_registry.register(TasksService)
