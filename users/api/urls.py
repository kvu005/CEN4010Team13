from rest_framework.routers import DefaultRouter
from django.urls import path, include
from users.api.views import UserViewSet

router = DefaultRouter()
router.register('users', UserViewSet, basename="users")

urlpatterns = [
    path('', include(router.urls)),
]
