from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Sender(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_sender(self):
        return self.user

class Receiver(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_receiver(self):
        return self.user

class Message(models.Model):
    sent = models.ForeignKey(Sender, on_delete=models.CASCADE)
    text = models.CharField(max_length=50)
    receive = models.ForeignKey(Receiver, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.text

    def get_routes(self):
        return f"Sent from {str(self.sent.user).upper()} to {str(self.receive.user).upper()}"

    