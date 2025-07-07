from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')       # columns to display
    list_filter = ('author', 'publication_year')                 # filter sidebar
    search_fields = ('title', 'author')                          # search bar
