from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=100)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.text

class Note(models.Model):
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE)
    text = models.TextField()

    class Meta:
        verbose_name_plural = "Notes"

    def __str__(self):
        return self.text[:10]