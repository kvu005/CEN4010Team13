from django.urls import path
from bookdetail import views

urlpatterns = [
    path('author/', views.author_list),
    path('author/<int:pk>/', views.author_detail),

    path('book/', views.book_list),
    path('book/<int:pk>/', views.book_detail),
]