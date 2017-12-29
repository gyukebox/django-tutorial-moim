import uuid
from django.db import models


class UserModel(models.Model):
    user_id = models.UUIDField(default=uuid.uuid4)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField()
    gender = models.CharField(max_length=1, default='M')

    def __str__(self):
        return self.name
