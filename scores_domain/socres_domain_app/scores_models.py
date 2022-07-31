from django.db import models
import uuid
import datetime
from django.db import models
from django.contrib.postgres.fields import ArrayField

class Scores(models.Model):
    scores_id = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        primary_key=True,
        editable=False
    )
    student_id = models.UUIDField()
    maths_score = models.IntegerField()
    science_score = models.IntegerField()
    social_sciences_score = models.IntegerField()
    english_score = models.IntegerField()
    second_language_score = models.IntegerField()
