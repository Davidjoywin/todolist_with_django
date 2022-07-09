from .models import User, Receiver, Sender, Message

david = User.objects.get(username="david")
mercy = User.objects.get(username="mercy")

david_as_receiver = Receiver.objects.get(user=david)
mercy_as_receiver = Receiver.objects.get(user=mercy)

david_as_sender = Sender.objects.get(user=david)
mercy_as_sender = Sender.objects.get(user=mercy)

# # david will send message to mercy
# message = Message.objects.create(sent=david_as_sender, text="I'm fine thanks for checking up, mercy!!", receive=mercy_as_receiver)
# message.save()

# # mercy will send message to david
# _message = Message.objects.create(sent=mercy_as_sender, text="you\'re welcome brother.", receive=david_as_receiver)
# _message.save()

for message in Message.objects.all():
    print(message, message.get_routes())