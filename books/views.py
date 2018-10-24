import time

from rest_framework import viewsets, mixins, serializers

from .models import Author, Book
from .serializers import AuthorListSerializer, AuthorDetailSerializer, BookSerializer

from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_401_UNAUTHORIZED
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticatedOrReadOnly


@api_view(["POST"])
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")

    user = authenticate(username=username, password=password)
    if not user:
        return Response({"error": "Login failed"}, status=HTTP_401_UNAUTHORIZED)

    token, _ = Token.objects.get_or_create(user=user)
    return Response({"token": token.key})


class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows books to be viewed
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)




class AuthorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows authors to be viewed
    """
    queryset = Author.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_serializer_class(self):
        if self.action == 'list':
            return AuthorListSerializer
        if self.action == 'retrieve':
            return AuthorDetailSerializer
        return AuthorDetailSerializer


