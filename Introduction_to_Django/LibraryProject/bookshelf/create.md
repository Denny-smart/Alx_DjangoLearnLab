<<<<<<< HEAD
>>> from bookshelf.models import Book
>>> #create
>>> book =Book.objects.create(title="1984", author="George Orwell",
 publication_year=1949)
>>> print(book)
1984 by George Orwell (1949)
>>> exit()

=======
```python
from bookshelf.models import Book

book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)
book
>>>>>>> d13de5bf52ee506da75b5cabc482d652413f9b94
