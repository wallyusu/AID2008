from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField('作者',max_length=50)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField('书名',max_length=50)
    author = models.ManyToManyField(Author)