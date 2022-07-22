from django.contrib import admin

from .models import Author, Book, Comments, Genre

# My registered models.
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Comments)
