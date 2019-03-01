from django.conf.urls import url
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from channels.auth import AuthMiddlewareStack
# from channels.staticfiles import StaticFilesConsumer
# routes defined for channel calls

# this is similar to the Django urls, but specifically for Channels

from simple_app.consumers import GetNewsConsumer

application = ProtocolTypeRouter({
    "websocket": AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter([
                url(r'^gql', GetNewsConsumer)
            ])
        )
    )
})
