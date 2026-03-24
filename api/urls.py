from django.urls import path 
from api.views.auth_views import RegisterView, ProfileView

urlpatterns = [
    path('api/register', RegisterView.as_view()),
    path('me/', ProfileView.as_view()),
]
