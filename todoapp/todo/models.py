from django.db import models

# Create your models here.
class TodoModel(models.Model):
    title=models.CharField(max_length=150)
    completed = models.BooleanField(default=False)
    tasked = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title