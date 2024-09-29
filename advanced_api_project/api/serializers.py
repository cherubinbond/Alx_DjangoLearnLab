from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'publication_year', 'author']

    # Custom validation for publication_year
    def validate_publication_year(self, value):
        if value > 2024:  # Adjust year based on the current year
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value
from .models import Author
from .serializers import BookSerializer

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']
# Serializer for the Book model
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'publication_year', 'author']

    # Custom validation for publication year
    def validate_publication_year(self, value):
        if value > 2024:  # Adjust this condition for future years
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

# Serializer for the Author model, including nested BookSerializer
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)  # Nested serialization for books

    class Meta:
        model = Author
        fields = ['name', 'books']
