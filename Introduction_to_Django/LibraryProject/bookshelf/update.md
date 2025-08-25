<<<<<<< HEAD
#update


>>> from bookshelf.models import Book
>>> book = Book.objects.get(title="1984")
>>> book.title = "Nineteen Eighty-Four"
>>> book.save()
>>> book
# <Book: Nineteen Eighty-Four>

=======
```python

book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
Book.objects.get(pk=book.pk)
# Expected output: <Book: Nineteen Eighty-Four by George Orwell (1949)>
>>>>>>> d13de5bf52ee506da75b5cabc482d652413f9b94
