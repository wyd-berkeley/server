from rest_framework import routers
from views import UserViewSet

router_v1 = routers.DefaultRouter(trailing_slash=False)
router_v1.register(r'user', UserViewSet)
