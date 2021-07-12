from django.db import models
from django.contrib.auth.models import User
class Goal(models.Model):
    specific = models.CharField(max_length=500)
    measureable = models.CharField(max_length=500)
    achievable = models.CharField(max_length=500)
    relevant = models.CharField(max_length=500)
    timely = models.CharField(max_length=500)
    overall_goal = models.CharField(max_length=500)
    notes = models.TextField(blank=True)
    owner = models.ForeignKey('users.User', related_name="goals", on_delete=models.CASCADE, null = True)

    def __str__(self):
        return self.overall_goal