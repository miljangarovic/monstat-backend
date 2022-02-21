from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Stanovnik,Grad,Godina


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class StanovnikSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stanovnik
        exclude = []


class GradSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grad
        exclude = []

