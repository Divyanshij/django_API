from django.urls import path
from . import views
urlpatterns = [
    path('books/', views.books),
    path('books',views.BookList.as_view()),
    path('books/<int:book_id>', views.Book.as_view())
]