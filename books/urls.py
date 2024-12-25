from django.urls import path
from .views import *

urlpatterns = [
    path('api/author/create/', AuthorCreateAPIView.as_view(), name='author_create'),
    path('api/author/list/', AuthorListAPIView.as_view(), name='author_list'),
    path('api/author/update/<int:id>/', AuthorUpdateAPIView.as_view(), name='author_update'),
    path('api/author/destroy/<int:id>/', AuthorDestroyAPIView.as_view(), name='author_destroy'),
    path('api/author/retrieve/<int:id>/', RetrieveAPIView.as_view(), name='author_retrieve'),
    path('api/books/create/', BookCreateAPIView.as_view(), name='book_create'),
    path('api/books/retrieve/<int:id>/', BookRetrieveAPIView.as_view(), name='book-retrieve'),
    path('api/books/update/<int:id>/', BookUpdateAPIView.as_view(), name='book_update'),
    path('api/books/destroy/<int:id>/', BookDestroyAPIView.as_view(), name='book_destroy'),
    path('api/books/list/', BookListAPIView.as_view(), name='book_list'),
    path('api/books/list/filter/', BookFilterAPIView.as_view(), name='book_list'),
]
