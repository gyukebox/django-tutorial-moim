from django_tutorial_moim.settings import STATIC_URL
from django.db import models
from user.models import UserModel


class MoimModel(models.Model):
    title = models.CharField(max_length=20)
    creator = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    starts_at = models.DateTimeField()
    max_attendee = models.PositiveIntegerField()
    attendees = models.ManyToManyField(UserModel, related_name='Attendee', blank=True)
    summary = models.CharField(max_length=100)
    description = models.TextField()
    image = models.FileField(blank=True, upload_to='static/images')
