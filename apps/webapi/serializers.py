from rest_framework import serializers
from .models import  Navigation
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'is_staff')


class NavSerializer(serializers.ModelSerializer):

    class Meta:
        model = Navigation
        fields = ('id', 'name', 'type', 'icon', 'uri')


