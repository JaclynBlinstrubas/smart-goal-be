from django.db import models

class User(models.Model):
    name = models.CharField(max_length=250)
    goal = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Goal(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="goals")
    specific = models.CharField(max_length=500)
    measureable = models.CharField(max_length=500)
    attainable = models.CharField(max_length=500)
    relevent = models.CharField(max_length=500)
    timely = models.CharField(max_length=500)
    overall_goal = models.CharField(max_length=500)

    def __str__(self):
        return self.author

class Notes(models.Model):
    body = models.TextField()
    
