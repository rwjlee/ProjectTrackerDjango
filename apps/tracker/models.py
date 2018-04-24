from django.db import models
from apps.user_info.models import User

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=128, null=False)
    user = models.ForeignKey(User, related_name='has_projects', on_delete=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'name')

class Task(models.Model):
    name = models.CharField(max_length=128, null=False)
    user = models.ForeignKey(User, related_name='has_tasks', null=True, on_delete=True)
    project = models.ForeignKey(Project, related_name='has_tasks', on_delete=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
