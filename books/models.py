from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=50)
    biography = models.CharField(max_length=100)

# class Genre(models.Model):
#     name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='author')
    published_date = models.DateField()
    genre = models.CharField(max_length=100)
# Create your models here.
