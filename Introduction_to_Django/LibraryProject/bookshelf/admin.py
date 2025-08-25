from django.contrib import admin
<<<<<<< HEAD

from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('publication_year',)
    search_fields = ('title', 'author')

admin.site.register(Book, BookAdmin)

=======
from .models import Book

# Custom admin view for Book
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Columns to show in admin list
    list_filter = ('publication_year',)                     # Adds filter sidebar by publication year
    search_fields = ('title', 'author')                     # Adds search box for title/author
>>>>>>> d13de5bf52ee506da75b5cabc482d652413f9b94
