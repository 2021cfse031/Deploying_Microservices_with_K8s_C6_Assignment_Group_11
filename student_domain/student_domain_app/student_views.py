from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import generics
from django.core import serializers
from rest_framework.response import Response
from rest_framework import status
import json
from student_domain_app.student_models import Student
from student_domain_app.student_serializers import StudentSerializers
import requests
# Create your views here.


class StudentListView(generics.ListCreateAPIView):
    serializer_class = StudentSerializers
    queryset = Student.objects.all()

class StudentDetailedView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StudentSerializers
    queryset = Student.objects.all()
