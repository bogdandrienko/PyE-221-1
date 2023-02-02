from django.contrib.auth.models import User, Group
from rest_framework import serializers
from django_app import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = ['username', 'email']
        fields = "__all__"


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Todo
        fields = "__all__"
