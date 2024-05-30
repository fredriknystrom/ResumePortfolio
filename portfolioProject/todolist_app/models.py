import uuid
from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    class Status(models.TextChoices):
        HIGH = '1', 'High'
        MEDIUM = '2', 'Medium'
        LOW = '3', 'Low'
        Done = '4', 'Done'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.MEDIUM)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.pk:
            self.user = kwargs.pop('user', None)
        super().save(*args, **kwargs)

    @staticmethod
    def get_priority(status):
        # Map status to priority levels
        status_priority = {
            Task.Status.HIGH: 1,
            Task.Status.MEDIUM: 2,
            Task.Status.LOW: 3,
            Task.Status.DONE: 4,
        }
        # Return priority level
        return status_priority.get(status, 5)  # Default to a higher value if status not found

    class Meta:
        ordering = ["status"]


   
