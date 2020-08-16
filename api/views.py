from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import StudentSerializer
from .models import Student


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all().order_by('name')
    serializer_class =StudentSerializer
