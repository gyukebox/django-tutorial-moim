import uuid
from django.db import models
from user.models import UserModel


class MoimModel(models.Model):
    moim_id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    title = models.CharField(max_length=20)
    creator = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    starts_at = models.DateTimeField()
    max_attendee = models.PositiveIntegerField()
    attendees = models.ManyToManyField(UserModel, related_name='Attendee')
    summary = models.CharField(max_length=100)
    description = models.TextField()
    image = models.FileField()
