from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Latihan
from .serializers import LatihanSerializer

class ListLatihanView(ListAPIView):
    queryset = Latihan.objects.all()
    serializer_class = LatihanSerializer