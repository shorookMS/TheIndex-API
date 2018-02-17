from rest_framework import viewsets, mixins

from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer


class BookViewSet(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    """
    API endpoint that allows books to be viewed or added
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class AuthorViewSet(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    viewsets.GenericViewSet):
    """
    API endpoint that allows authors to be viewed or added
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
