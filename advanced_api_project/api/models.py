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
# Author model represents the book author, containing just a name field.
class Author(models.Model):
    name = models.CharField(max_length=100)
    # String representation to return the name in a readable format.
    def __str__(self):
        return self.name

# Book model represents a book authored by an Author.
class Book(models.Model):
    title = models.CharField(max_length=200)  # The book's title
    publication_year = models.IntegerField()  # Year when the book was published
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    # String representation to return the book title.
    def __str__(self):
        return self.title

