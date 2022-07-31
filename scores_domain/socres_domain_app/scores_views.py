from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import generics
from django.core import serializers
from rest_framework.response import Response
from rest_framework import status
import json
from socres_domain_app.scores_models import Scores
from socres_domain_app.scores_serializers import ScoresSerializers
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
# Create your views here.

class ScoresListView(generics.ListCreateAPIView):
    serializer_class = ScoresSerializers
    queryset = Scores.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['student_id']

class ScoresDetailedView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ScoresSerializers
    queryset = Scores.objects.all()


# Create your views here.
