from rest_framework import generics, permissions, filters
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters import rest_framework
from django_filters.rest_framework import DjangoFilterBackend


class BookListView(generics.ListAPIView):
    """
    Provides a list of all books, with support for filtering, searching, and ordering.

    Filtering fields:
    - title (exact match)
    - publication_year
    - author (author ID)

    Searchable fields:
    - title
    - author's name

    Orderable fields:
    - title
    - publication_year
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

    # Enable filter, search, and ordering backends
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    # Filtering
    filterset_fields = ["title", "publication_year", "author"]

    # Search (partial match)
    search_fields = ["title", "author__name"]

    # Ordering
    ordering_fields = ["title", "publication_year"]
    ordering = ["title"]  # Default ordering


# DetailView - GET /books/<pk>/
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# CreateView - POST /books/
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can create


# UpdateView - PUT/PATCH /books/<pk>/
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


# DeleteView - DELETE /books/<pk>/
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
