from django.db import models
from django.shortcuts import render
from rest_framework import generics

from .models import Book
from .serializer import BooksSerializer
from .permissions import IsAuthorOrReadOnly

# Create your views here.
class BooksListView(generics.ListCreateAPIView):    
    serializer_class = BooksSerializer
    queryset = Book.objects.all()


class BookDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BooksSerializer
    queryset = Book.objects.all()
    permission_classes = (IsAuthorOrReadOnly,)
