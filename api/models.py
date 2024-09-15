from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

from .models import Author
from .serializers import BookSerializer

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields =['name', 'books']

# The Author model represents an author with a one-to-many relationship to books.
class Author(models.Model):
    name = models.CharField(max_length=100)
    # String representation of the author, displaying the name.
    def __str__(self):
        return self.name

# The Book model stores information about books, with a foreign key to Author.
class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    # String representation of the book, displaying the title.
    def __str__(self):
        return self.title





