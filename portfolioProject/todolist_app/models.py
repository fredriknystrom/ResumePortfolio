import uuid
from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    class Priority(models.TextChoices):
        HIGH = 'high', 'High'
        MEDIUM = 'medium', 'Medium'
        LOW = 'low', 'Low'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    priority = models.CharField(max_length=10, choices=Priority.choices, default=Priority.MEDIUM)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.pk:
            self.user = kwargs.pop('user', None)
        super().save(*args, **kwargs)


   
