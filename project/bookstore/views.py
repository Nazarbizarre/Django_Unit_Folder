from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect

from .models import Genre, Book, Author

def home(request):
    genres = Genre.objects.all()
    books = Book.objects.all()
    data = {"genres": genres, "books": books} 
    return render(request, "index.html", context=data)

def book_info(request, book_id):
  book = get_object_or_404(Book, id=book_id)
  genres = Genre.objects.all()
  # author = book.author.all()
  if request.method == "POST":
    book.delete()
    messages.success(request, f'Book: {book.title} has been deleted successfully')
    return redirect("bookstore:home")
  return render(request, "book_info.html", {'book':book, "genres":genres})

def get_books_by_genre(request, genre_id):
  genres = Genre.objects.all()
  genre = get_object_or_404(Genre, id=genre_id)
  books = Book.objects.filter(genre=genre)
  data = {"genres":genres, "books":books}
  return render(request, 'index.html', context=data)

def get_books_by_author(request, author_id):
  genres = Genre.objects.all()
  authors = Genre.objects.all()
  author = get_object_or_404(Author, id=author_id)
  books = Book.objects.filter(author=author)
  data = {"authors":authors, "books":books, "genres":genres}
  return render(request, 'index.html', context=data)

def create_book(request):
  genres = Genre.objects.all()
  if request.method == 'POST':
    title = request.POST.get('title')
    description = request.POST.get('description')
    genre_id = request.POST.get('genre')
    genre = get_object_or_404(Genre, id=int(genre_id))
    date_published = request.POST.get('date_published')

    try:
      book = Book(title=title, description=description, genre=genre, publishing_date=datetime.strptime(date_published, '%m/%d/%Y'))
      book.full_clean()  
    except Exception as e:
        print(e)
        return HttpResponse('<h1>Bad Values</h1>')
    else:
      book.save()
      messages.success(request, f'Book: {book.title} has been created successfully')
      return redirect('bookstore:home')
  return render(request, "create_book.html", context={"genres":genres})