from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterView, UserViewSet, ProfileView

router = DefaultRouter()
router.register('posts', UserViewSet, basename='users')

urlpatterns = [
    path("", include(router.urls)),
    path('register/', RegisterView.as_view()),
    path('profile/', ProfileView.as_view()),
]
