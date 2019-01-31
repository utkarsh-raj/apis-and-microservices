from django.db import models

# Create your models here.

class ExerciseUser(models.Model):
    name = models.CharField(max_length=500, default=1)

    def __str__(self):
        return self.name

class Exercise(models.Model):
    user = models.ForeignKey(ExerciseUser, on_delete=models.CASCADE)
    description = models.CharField(max_length=1000, default=1)
    duration = models.IntegerField(blank=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description