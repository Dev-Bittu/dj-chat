from channels.consumer import SyncConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync
from .models import Chat, Group

class ChatConsumer(SyncConsumer):
	def websocket_connect(self, event):
		self.group_name = self.scope['url_route']['kwargs']['group_name'] #getting group_name from request (scope) and setting it to public
		async_to_sync(self.channel_layer.group_add)(
			self.group_name,
			self.channel_name
		) #adding/creating group
		self.send({
			'type': 'websocket.accept'
		}) #accepting user
		
	
	def websocket_disconnect(self, event):
		async_to_sync(self.channel_layer.group_discard)(
			self.group_name,
			self.channel_name
		) #discarding user from group before disconnect
		raise StopConsumer() #close connection from user
	
	def websocket_receive(self, event):
		
		async_to_sync(self.channel_layer.group_send)(
		self.group_name, 
		{
			'type': 'chat.message',
			'message': event
		}) #send incoming message to group
		group = Group.objects.get(name=self.group_name)
		chat = Chat(msg = event['text'],group=group)
		chat.save()
		
	def chat_message(self, event):
		self.send({
		'type': 'websocket.send',
		'text':	event['message']['text']
		}) #send message to every user of group
		
		print('msg send...', event['message']['text'], type(event['message']))
	