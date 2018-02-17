from django.db import models


class Author(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    imageUrl = models.CharField(max_length=255, blank=True, default="")

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name

    class Meta:
        ordering = ['-last_name', '-first_name']


class Book(models.Model):
    COLOR_CHOICES = (
        ('R', 'red'),
        ('B', 'blue'),
        ('G', 'green'),
        ('Y', 'yellow'),
        ('K', 'black'),
        ('W', 'white'),
        ('Gr', 'grey'),
    )
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    available = models.BooleanField(default=True)
    color = models.CharField(max_length=2, choices=COLOR_CHOICES)
    authors = models.ManyToManyField(Author, related_name='books')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-title', ]
