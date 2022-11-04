from django.urls import path
from ratingscomments import views

urlpatterns = [
    path('author/', views.author_list),
    path('author/<int:pk>/', views.author_detail),

    path('book/', views.book_list),
    path('book/<int:pk>/', views.book_detail),

    path('user/', views.user_list),
    path('user/<int:pk>/', views.user_detail),

    path('comment/', views.comment_list),
    path('comment/<int:pk>/', views.comment_detail),

    path('rating/', views.rating_list),
    path('rating/<int:pk>/', views.rating_detail),
]