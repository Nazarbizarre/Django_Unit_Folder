from django.urls import path, include

from .views import home, book_info, get_books_by_genre, create_book

app_name = 'bookstore'

urlpatterns = [
    path('', home, name='home'),
    path('book/<int:book_id>', book_info, name="book_info"),
    path("genre/<int:genre_id>", get_books_by_genre, name="get_books_by_genre"),
    path('create_book/', create_book, name="create_book")
]