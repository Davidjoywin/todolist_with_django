from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Sender(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        self.user.username

class Receiver(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __self__(self):
        self.user.username

class Message(models.Model):
    sent = models.ForeignKey(Sender, on_delete=models.CASCADE)
    text = models.CharField(max_length=50)
    receive = models.ForeignKey(Receiver, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.text

    