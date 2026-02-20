from rest_framework import serializers
from teachers.models import Teacher
from student.models import Student
from mentor.models import Mentor
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class MentorSerializer(serializers.ModelSerializer):
    students = StudentSerializer(many=True) #The field name shoule be same as the related name
    class Meta:
        model = Mentor
        fields = '__all__'