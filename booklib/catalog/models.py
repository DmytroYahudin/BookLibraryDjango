from django.db import models
from django.conf import settings

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Genre(models.Model):
    genre = models.CharField(max_length=20, help_text="Enter a book genre")

    def __str__(self):
        return self.genre


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField()
    genre = models.ManyToManyField(Genre, help_text="Select a genre", blank=True)
    image = models.ImageField(blank=True, null=True)
    number_of_views = models.IntegerField(default=0)

    class Meta:
        ordering = ['-number_of_views']

    def __str__(self):
        return self.title


class Comments(models.Model):
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)
    for_book = models.ForeignKey(Book, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'comments'


    def __str__(self):
        return self.comment
