from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    
    class Roles(models.TextChoices):
        ADMIN = "admin", "Admin"
        MEMBER = "member", "Member"
        
    role = models.CharField(
        max_length=10,
        choices=Roles.choices,
        default=Roles.MEMBER,
    )