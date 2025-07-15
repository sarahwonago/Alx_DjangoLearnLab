from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import (
    RegisterView,
    list_books_view,
    LibraryDetailView
)

urlpatterns = [
    path('books/', list_books_view, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    # Authentication routes
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
]

