from django.urls import path, include
from . import views

urlpatterns = [   # path('' , THE FUNCTION TO BE SEND TO, NAME = TAMPLETNAME)
    path('', views.index, name='index'),  # Homepage --> index.html
    path('books/', views.books, name='books_list'),  # BookList --> booklist.html
    path('book/<int:bId>/', views.book, name='book_detail'), #BookDetails --> book.html
]