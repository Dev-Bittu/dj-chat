from django.urls import path
from ws import consumers

ws_urlpatterns = [
	path('room/<str:group_name>/', consumers.ChatConsumer.as_asgi())
]