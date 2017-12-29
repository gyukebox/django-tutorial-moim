import uuid
from django.db import models


class UserModel(models.Model):
    user_id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=13)
    age = models.PositiveSmallIntegerField()
    gender = models.CharField(max_length=1, default='M')
