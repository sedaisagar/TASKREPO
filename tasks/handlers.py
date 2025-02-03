from django_socio_grpc.services.app_handler_registry import AppHandlerRegistry
from tasks.services import TasksService


def grpc_handlers(server):
    app_registry = AppHandlerRegistry("tasks", server)
    app_registry.register(TasksService)
