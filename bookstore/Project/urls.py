from django.urls import path
from Project import views

urlpatterns = [
    path('author/', views.author_list),
    path('author/<int:pk>/', views.author_detail),

    path('book/', views.book_list),
    path('book/<int:pk>/', views.book_detail),
    path('genre/<str:feature>/',views.genre),
    path('top_seller/',views.top_seller),
    path('rating/<int:feature>/',views.rating),
]