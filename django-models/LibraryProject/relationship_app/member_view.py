from django.shortcuts import render
from .models import UserProfile

# Role check helper
def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'


