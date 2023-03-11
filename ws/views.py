from django.shortcuts import render
from .models import Group, Chat

# Create your views here.
def ws(request, group_name):
	group = Group.objects.filter(name=group_name).first()
	if group:
		chats = Chat.objects.all()
	else:
		group = Group(name=group_name)
		group.save()
		chats = []
	print(chats)
	return render(request, 'ws/chat.html', {'group_name': group_name, 'chats': chats})