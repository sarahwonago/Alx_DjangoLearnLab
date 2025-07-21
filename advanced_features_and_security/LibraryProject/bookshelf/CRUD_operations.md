# Permissions and Groups Setup Guide

## Custom Permissions

Defined in `Book` model:

- can_view
- can_create
- can_edit
- can_delete

## Groups and Assigned Permissions

| Group   | Permissions                                |
| ------- | ------------------------------------------ |
| Viewers | can_view                                   |
| Editors | can_view, can_create, can_edit             |
| Admins  | can_view, can_create, can_edit, can_delete |

## View Protection

- `book_list`: requires `can_view`
- `book_create`: requires `can_create`
- `book_edit`: requires `can_edit`
- `book_delete`: requires `can_delete`

# CRUD Operations for Book Model in Django Shell

This document demonstrates how to create, retrieve, update, and delete a `Book` instance using Django’s ORM via the Django shell.

---

## Create a Book Instance

```python
from bookshelf.models import Book

# Create a new book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(book)
```

**Expected Output:**

```
1984 by George Orwell (1949)
```

---

## Retrieve the Book

```python
from bookshelf.models import Book

# Retrieve the created book
book = Book.objects.get(title="1984")
print(book.title, book.author, book.publication_year)
```

**Expected Output:**

```
1984 George Orwell 1949
```

---

## Update the Book Title

```python
from bookshelf.models import Book

# Update the title of the book
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
print(book.title)
```

**Expected Output:**

```
Nineteen Eighty-Four
```

---

## Delete the Book

```python
from bookshelf.models import Book

# Delete the book instance
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Confirm deletion
print(Book.objects.all())
```

**Expected Output:**

```
<QuerySet []>
```

---
