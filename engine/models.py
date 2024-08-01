import uuid

from django.db import models

from account.models import User

# Create your models here.
class Engine(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4 , editable=False)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    
    created_by = models.ForeignKey(User, related_name='lists', on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title