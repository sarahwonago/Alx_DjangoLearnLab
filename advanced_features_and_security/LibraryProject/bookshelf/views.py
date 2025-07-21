from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect
from .models import Book
from .forms import ExampleForm, SearchForm


@permission_required("bookshelf.view_book", raise_exception=True)
def book_list(request):
    form = SearchForm(request.GET or None)
    books = Book.objects.all()

    if form.is_valid():
        search_term = form.cleaned_data["search"]
        books = books.filter(title__icontains=search_term)

    return render(request, "bookshelf/book_list.html", {"form": form, "books": books})


@permission_required("bookshelf.add_book", raise_exception=True)
def book_create(request):
    if request.method == "POST":
        form = ExampleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = ExampleForm()
    return render(request, "bookshelf/book_form.html", {"form": form})
