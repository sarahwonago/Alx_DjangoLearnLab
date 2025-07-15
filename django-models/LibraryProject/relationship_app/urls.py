from django.urls import path
from .views import (
    RegisterView,
    CustomLoginView,
    CustomLogoutView,
    list_books_view,
    LibraryDetailView
)

urlpatterns = [
    path('books/', list_books_view, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    # Authentication routes
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
]

