from django.urls import path
from ws import consumers

ws_urlpatterns = [
	path('room/<str:group_name>/', consumers.Chat.as_asgi())
]