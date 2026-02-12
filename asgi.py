import os
import django
from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "neulibrary.settings")
django.setup() # Vital for model access

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

# Import routing from both apps
import cctv.routing
import ems.routing

application = ProtocolTypeRouter({
    # Handles standard web pages
    "http": get_asgi_application(),
    
    # Handles all real-time traffic
    "websocket": AuthMiddlewareStack(
        URLRouter(
            # Merge lists using '+'
            cctv.routing.websocket_urlpatterns + 
            ems.routing.websocket_urlpatterns
        )
    ),
})
