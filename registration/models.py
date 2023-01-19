from django.db import models
import uuid


class register(models.Model):
    user_id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_name=models.CharField(max_length=20)
    user_password=models.CharField(max_length=10)

class team_register(models.Model):
    team_id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    team_name=models.CharField(max_length=10)
    team_email=models.CharField(max_length=20)
    team_password=models.CharField(max_length=10)

# Create your models here.
