from rest_framework import generics
from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import BookSerializer
from .models import Book


class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
