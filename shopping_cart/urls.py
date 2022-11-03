from django.urls import path
from shopping_cart import views
 
urlpatterns = [
 path('shopping_cart/', views.shopping_cart_list),
 path('shopping_cart/<int:pk>/', views.shopping_cart_detail),

]