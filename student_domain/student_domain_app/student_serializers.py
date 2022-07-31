from rest_framework import serializers
from student_domain_app.student_models import Student

class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
