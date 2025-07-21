from django.shortcuts import render
from .models import UserProfile

# Role check helpers
def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

