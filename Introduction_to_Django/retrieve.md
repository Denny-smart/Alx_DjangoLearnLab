```python

Book.objects.all()
# Expected output: <QuerySet [<Book: 1984 by George Orwell (1949)>]>
book = Book.objects.get(title="1984")
print(book.author, book.publication_year)
# Expected output: George Orwell 1949
