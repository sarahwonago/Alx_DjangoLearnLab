from django import forms
from .models import Book


class ExampleForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "publication_year"]


class SearchForm(forms.Form):
    search = forms.CharField(required=False, label="Search by title")
