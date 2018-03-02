from rest_framework import serializers
from .models import Author, Book


class BookSerializer(serializers.ModelSerializer):
    color = serializers.SerializerMethodField()

    class Meta:
        model = Book
        exclude = ('authors',)

    def get_color(self, obj):
        return obj.get_color_display()


class BookListingField(serializers.RelatedField):
    def to_representation(self, value):
        return {
            "title": value.title,
            "url": value.get_absolute_url()
        }


class AuthorListSerializer(serializers.ModelSerializer):
    books = BookListingField(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'first_name', 'last_name', 'imageUrl', 'books']


class AuthorDetailSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'first_name', 'last_name', 'imageUrl', 'books']
