from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import Navigation
from . import serializers
from django.http.response import JsonResponse
from .permissions import IsAdmin, ReadOnly
from django.contrib.auth.models import User



class UserViewSet(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

# ListAPIView is intentional (POST not allowed) so navigation links can only be made in admin and tied to roles
class NavList(generics.ListAPIView):

    serializer_class = serializers.NavSerializer

    def get_queryset(self):
        if self.request.user.is_staff:
            self.queryset = Navigation.objects.all()
            return self.queryset
        elif not self.request.user.is_staff:
            self.queryset = Navigation.objects.exclude(type='admin')
            return self.queryset
    queryset = get_queryset


class NavDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Navigation.objects.all()
    serializer_class = serializers.NavSerializer


