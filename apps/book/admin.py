from django.contrib import admin

from .apps import BookConfig
from .models import Book

admin.site.register(Book)
