from django.contrib import admin
from django.urls import path, include
from .views import UserRUDView, UserView, LoginView

urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
    path('user/<int:id>', UserRUDView.as_view()),
	path('user/', UserView.as_view()),
    path('login/', LoginView.as_view()),
]