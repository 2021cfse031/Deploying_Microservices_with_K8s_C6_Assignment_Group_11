from django.db import models
import uuid
import datetime
from django.db import models
from django.contrib.postgres.fields import ArrayField

class Student(models.Model):
    category_otions = (
    ("male","male"),
    ("female","female"),
    ("other","other")
    )
    student_id = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        primary_key=True,
        editable=False
    )
    student_first_name = models.CharField(max_length=100, blank=False, null = False)
    student_second_name = models.CharField(max_length=100, blank=False, null = False)
    student_gender = models.CharField(max_length=12,choices=category_otions,default="female")
    student_roll_number = models.IntegerField()
