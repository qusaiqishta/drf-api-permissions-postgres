from django.urls import path

from .views import BooksListView, BookDetailsView

urlpatterns = [
    path('', BooksListView.as_view(), name='posts_api'), # /api/v1/books/
    path('<int:pk>', BookDetailsView.as_view(), name='post_details_api'), # /api/v1/books/<int:pk>
]