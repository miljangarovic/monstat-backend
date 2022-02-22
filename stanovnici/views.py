from django.shortcuts import render
from .models import Stanovnik
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import serializers
from stanovnici.serializers import UserSerializer, GroupSerializer, StanovnikSerializer, GradSerializer
from .models import Grad
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class StanovnikViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Stanovnik.objects.select_related('grad_id').all()
    serializer_class = StanovnikSerializer
    # permission_classes = [permissions.IsAuthenticated]


def gradovi(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        gradovi = Grad.objects.all()
        serializer = GradSerializer(gradovi, many=True)
        return JsonResponse(serializer.data, safe=False, status=200)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = GradSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


def stanovnici(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        stanovnici = Stanovnik.objects.all()
        serializer = StanovnikSerializer(stanovnici, many=True)
        print(serializer)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = StanovnikSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
