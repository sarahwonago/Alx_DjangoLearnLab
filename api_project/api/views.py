from rest_framework.generics import ListApiView

from .serializers import BookSerializer
from .models import Book


class BookListView(ListApiView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
