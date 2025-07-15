from django.db import models

class Book(models.Model):
    """Model representing a book in the library."""
    title = models.CharField(max_length=200, help_text='Enter the book title')
    author = models.CharField(max_length=100, help_text='Enter the author name')
    publication_year = models.IntegerField(help_text='Enter the year of publication')

    def __str__(self):
        """String representation of the Book model."""
        return f"{self.title} by {self.author} ({self.publication_year})"
