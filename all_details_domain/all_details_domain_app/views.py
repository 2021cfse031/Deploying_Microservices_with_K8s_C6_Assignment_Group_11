from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import generics
from django.core import serializers
from rest_framework.response import Response
from rest_framework import status
import json
import requests

# Create your views here.


@api_view(['POST'])
def student_scores_view(request):
    if request.method == 'POST':
        URL_student = "http://127.0.0.1:7000/student/" + \
            request.data["student_id"]
        r_student = requests.get(url=URL_student)
        data_student_json = r_student.json()
        URL_score = "http://127.0.0.1:8000/scores?student_id=" + \
            request.data["student_id"]
        r_score = requests.get(url=URL_score)
        data_score_json = r_score.json()
        data_student_json["scores"] = data_score_json
        return Response(data=data_student_json, status=status.HTTP_200_OK)
