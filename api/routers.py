from rest_framework.routers import DefaultRouter
from api.views.user_viewsets import UserViewSet

router = DefaultRouter()

router.register("users", UserViewSet, basename="users")