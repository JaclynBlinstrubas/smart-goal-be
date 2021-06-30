from django.db import models

class User(models.Model):
    your_name = models.CharField(max_length=250)
    specific = models.CharField(max_length=500)
    measureable = models.CharField(max_length=500)
    achievable = models.CharField(max_length=500)
    relevent = models.CharField(max_length=500)
    timely = models.CharField(max_length=500)
    
    def __str__(self):
        return self.name

class Goal(models.Model):
    overall_goal = models.CharField(max_length=500)
  
    def __str__(self):
        return self.overall_goal

class Notes(models.Model):
    notes = models.TextField()

    def __str__(self):
        return self.notes
    
