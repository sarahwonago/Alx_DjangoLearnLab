from .views import BookListView
from django.urls import path

urlpatterns = [
    path("books/", BookListView.as_view(), name="book-list"),
]
