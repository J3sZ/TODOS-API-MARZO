from django.shortcuts import render
from .models import task
from .serializers import TaskSerializer
from rest_framework import generics


# Create your views here.

class taskList(generics.ListCreateAPIView): 
    queryset = task.objects.all()
    serializer_class = TaskSerializer

class taskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = task.objects.all()
    serializer_class = TaskSerializer
