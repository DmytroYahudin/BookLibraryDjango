from django.contrib import admin
from .models import Author, Book, Genre, Comments

# My registered models.
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Comments)
