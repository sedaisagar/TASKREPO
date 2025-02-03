from django.db import models
from utils.enums import STATUSES


class Tasks(models.Model):
    """
    Task Payload Sample:
    {
        "email" : "abc@getnada.com",
        "subject": "Successfully Registered",
        "body": "Welcome to the new world of exploration!",
    }
    """

    data = models.JSONField(default=dict)
    status = models.CharField(choices=STATUSES, default="pending", max_length=10)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created_at",)
