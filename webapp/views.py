from django.shortcuts import render
from .serializers import myModelSerializer
from .models import myModel
from rest_framework import generics

class myModelList(generics.ListCreateAPIView):
    queryset = myModel.objects.all()
    serializer_class = myModelSerializer