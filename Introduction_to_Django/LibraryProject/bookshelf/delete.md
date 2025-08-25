#delete

<<<<<<< HEAD
>>> from bookshelf.models import Book
>>> book.delete()
# (1, {'bookshelf.Book': 1})
>>> print(Book.objects.all())
<QuerySet []>

=======
from bookshelf.models import Book book.delete()

(1, {'bookshelf.Book': 1})
print(Book.objects.all()) <QuerySet []>
>>>>>>> d13de5bf52ee506da75b5cabc482d652413f9b94
