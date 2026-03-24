from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from apps.users.models import User
from api.serializers.user_serializers import UserSerializer
from apps.users.permissions import IsAdmin

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def get_permissions(self):
        if self.action == "list":
            return [IsAdmin()]
        return [IsAuthenticated()]