from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    # Using re_path with a named group (?P<camera_id>\w+) 
    # This allows any alphanumeric ID (camera1, cam_basement, etc.)
    # re_path(r'ws/video/(?P<camera_id>\w+)/$', consumers.VideoConsumer.as_asgi()),
    # re_path(r'ws/video/$', consumers.VideoConsumer.as_asgi()),
    re_path(r'ws/video/(?P<camera_id>\w+)/$', consumers.VideoConsumer.as_asgi()),
    
    # You can add more specific routes here later
    # example: re_path(r'ws/plate-alerts/$', consumers.PlateAlertConsumer.as_asgi()),
]
