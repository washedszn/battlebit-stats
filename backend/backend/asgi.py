from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
import battlebit.routing

application = ProtocolTypeRouter({
  "http": get_asgi_application(),
  "websocket": URLRouter(
        battlebit.routing.websocket_urlpatterns
    ),
})