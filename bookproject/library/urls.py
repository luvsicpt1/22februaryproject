from django.urls import path
from .views import (
    AuthorListCreateView,
    BookListCreateView,
    BookDeleteView,
)

urlpatterns = [
    path("authors/", AuthorListCreateView.as_view(), name="author-list"),
    path("books/", BookListCreateView.as_view(), name="book-list"),
    path("books/<int:pk>/", BookDeleteView.as_view(), name="book-delete"),
]