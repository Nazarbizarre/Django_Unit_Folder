from datetime import datetime
from django.db import models
from django.urls import reverse


class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
class Author(models.Model):
    name = models.CharField(max_length=50)
    
    class Meta:
        ordering = ["name"]
        
    def __str__(self):
        return self.name
    
class Book(models.Model):
    class Type(models.TextChoices):
        PAPER = "Paper", "PAPER"
        DIGITAL = "Digital", "DIGITAL"
    
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    added = models.DateTimeField(auto_now_add=True)
    publishing_date = models.DateField(auto_now=True)
    isbn = models.CharField(max_length=17, default="111-2-3333-4444-5")
    price = models.FloatField(default=1.0)
    author = models.ManyToManyField(Author, related_name="books")
    
    type = models.CharField(
        max_length=7,
        choices=Type,
        default=Type.PAPER
    )
    
    genre = models.ForeignKey(
        Genre,
        on_delete=models.CASCADE,
        related_name="books"
    )
    
    class Meta:
        ordering = ['title']
        indexes= [
            models.Index(fields=['title'])
        ]
        
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('bookstore:book_info', args=[self.id])
    