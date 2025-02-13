from django.urls import path, include

from .views import home, book_info, get_books_by_genre, create_book, get_books_by_author

app_name = 'bookstore'

urlpatterns = [
    path('', home, name='home'),
    path('book/<int:book_id>', book_info, name="book_info"),
    path("genre/<int:genre_id>", get_books_by_genre, name="get_books_by_genre"),
    path('create_book/', create_book, name="create_book"),
    path("authot/<int:author_id>", get_books_by_author, name="get_books_by_author"),
]