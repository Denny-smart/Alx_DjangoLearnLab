from django.db import models

<<<<<<< HEAD
=======
# Create your models here.
from django.db import models

>>>>>>> d13de5bf52ee506da75b5cabc482d652413f9b94
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return f"{self.title} by {self.author} ({self.publication_year})"
