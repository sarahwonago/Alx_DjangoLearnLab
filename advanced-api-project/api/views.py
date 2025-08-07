from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer


# ListView - GET /books/
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [
        permissions.AllowAny
    ]  # Allow unauthenticated access for reading


# DetailView - GET /books/<pk>/
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# CreateView - POST /books/
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]  # Only authenticated users can create


# UpdateView - PUT/PATCH /books/<pk>/
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


# DeleteView - DELETE /books/<pk>/
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
