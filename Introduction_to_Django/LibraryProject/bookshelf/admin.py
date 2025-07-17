from django.contrib import admin
from .models import Book

# Custom admin view for Book
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Columns to show in admin list
    list_filter = ('publication_year',)                     # Adds filter sidebar by publication year
    search_fields = ('title', 'author')                     # Adds search box for title/author
