```python

book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
Book.objects.get(pk=book.pk)
# Expected output: <Book: Nineteen Eighty-Four by George Orwell (1949)>
