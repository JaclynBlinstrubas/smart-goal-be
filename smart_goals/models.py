from django.db import models
class Goal(models.Model):
    specific = models.CharField(max_length=500)
    measureable = models.CharField(max_length=500)
    achievable = models.CharField(max_length=500)
    relevant = models.CharField(max_length=500)
    timely = models.CharField(max_length=500)
    overall_goal = models.CharField(max_length=500)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.overall_goal