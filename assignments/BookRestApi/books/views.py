from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

# Create (POST) and List (GET all)
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Retrieve (GET), Update (PUT/PATCH), and Delete (DELETE) a book
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
