from rest_framework import serializers

from .models import Book

class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'subtitle', 'author', 'isbn')
        model = Book