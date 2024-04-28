from django.urls import path

from ws1.consumers import MySynceConsumer, MyAsynceConsumer

websocket_urlpatterns = [
    path(
        "ws/sc/",
        MySynceConsumer.as_asgi(),
    ),
    path(
        "ws/ac/",
        MyAsynceConsumer.as_asgi(),
    ),
]
