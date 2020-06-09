from django.urls import path, include
from .views import ListLatihanView

urlpatterns = [
    path('latihan/', ListLatihanView.as_view())
]