from django.db.models import Model
from rest_framework import serializers
from .models import Course, People
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = 'id', 'username', 'first_name', 'last_name', 'email','is_staff', 'is_active'
        view_name = 'user'


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = 'id', 'name', 'description'
        view_name = 'course'


class PeopleSerializer(serializers.ModelSerializer):
    user_data = UserSerializer(source='user',read_only=True)

    class Meta:
        model = People
        fields = 'id', 'user', 'is_teacher', 'user_data'
        view_name = 'people'





