from django.db import models
from utils.enums import STATUSES

from task_processor_ms.tasks import email_sender


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

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # add task for email sender when create
        if self.status == "pending":
            email_sender.delay(self.data, pk=self.pk)
