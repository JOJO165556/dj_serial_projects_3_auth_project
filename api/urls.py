from django.urls import path 
from api.views.auth_views import RegisterView, ProfileView, LogoutView

urlpatterns = [
    path('register', RegisterView.as_view()),
    path('me/', ProfileView.as_view()),
    path("logout/", LogoutView.as_view()),
]
