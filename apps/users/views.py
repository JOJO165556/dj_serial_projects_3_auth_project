from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from users.permissions import IsAdmin, IsOwner
from rest_framework.views import APIView
from users.models import User

class AdminOnlyView(APIView):
    permission_classes = [IsAuthenticated, IsAdmin]
    
    def get(self, request):
        return Response({"message": "admin only"})

class UserDetailView(APIView):
    permission_classes = [IsAuthenticated, IsOwner]
    
    def get(self):
        return User.objects.get(id=self.kwargs["id"])
    
    def put(self, request, id):
        user = self.get_object()
        self.check_object_permissions(request, user)
        
        user.username = request.data.get("username", user.username)
        user.save()
        return Response({"message": "updated"})