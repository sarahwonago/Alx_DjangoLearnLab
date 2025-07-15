from .models import Author, Book, Library, Librarian

author1 = Author.objects.create(name='J.K. Rowling')

book1 = Book.objects.create(title='Harry Potter and the Philosopher\'s Stone', author=author1)
book2 = Book.objects.create(title='Harry Potter and the Chamber of Secrets', author=author1)
library1 = Library.objects.create(name='Central Library')
library1.books.add(book1, book2)

librarian1 = Librarian.objects.create(name='John Doe', library=library1)

# query a book by a specific author
books_by_author = Book.objects.filter(author__name='J.K. Rowling')

# list all books in a library
books_in_library = library1.books.all()

# retrieve the librarian of a specific library
librarian_of_library = library1.librarian