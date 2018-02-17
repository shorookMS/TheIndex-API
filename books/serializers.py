from rest_framework import serializers
from .models import Author, Book


class BookSerializer(serializers.ModelSerializer):
    color = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = '__all__'

    def get_color(self, obj):
        return obj.get_color_display()


class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = '__all__'
