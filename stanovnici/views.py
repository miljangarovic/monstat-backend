from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from .models import Stanovnik
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from stanovnici.serializers import UserSerializer, StanovnikSerializer, GradSerializer
from .models import Grad

@api_view(['GET'])
def getUsers(request):
    users = User.objects.all().order_by('-date_joined')
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data, status=200)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def registerUser(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            return Response({"message": "Uspjesno dodat novi korisnik!"}, status=200)
        return Response({"message": "Neuspjesno dodat novi korisnik!"}, status=400)


@api_view(['GET'])
def getRoutes(request):
    routes = [
        {'GET': '/api/people'},
        {'POST': '/api/people'},
        {'GET': '/api/cities'},
    ]
    return Response(routes)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def gradovi(request):
    """
    List all cities, or create a new city.
    """

    if request.method == 'GET':
        gradovi = Grad.objects.all()
        serializer = GradSerializer(gradovi, many=True)
        return Response(serializer.data, status=200)

    elif request.method == 'POST':
        data = request.data
        grad = Grad.objects.create(naziv=data['naziv'])
        serializer = GradSerializer(data=data, many=False)
        if serializer.is_valid():
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)


@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def updateOrDeleteGrad(request, pk):
    """
    Update or delete the city.
    """

    if request.method == 'PUT':
        data = request.data
        grad = get_object_or_404(Grad, id=pk)
        grad.naziv = data['naziv']
        grad.save()
        serializer = GradSerializer(grad, many=False)
        return Response(serializer.data, status=200)

    elif request.method == 'DELETE':
        grad = get_object_or_404(Grad, id=pk)
        grad.delete()
        return Response(status=200)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def stanovnici(request):
    """
    List all people, or create a persone.
    """
    if request.method == 'GET':
        stanovnici = Stanovnik.objects.all()
        serializer = StanovnikSerializer(stanovnici, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = request.data
        stanovnik = Stanovnik.objects.create(ime=data['ime'], grad_id=data['grad_id'],
                                             godina_id=data['godina_id'],
                                             pol_id=data['pol_id'], drzavljanstvo_id=data['drzavljanstvo_id'],
                                             nacionalnost_id=data['nacionalnost_id'],
                                             jezik_id=data['jezik_id'],
                                             vjeroispovijest_id=data['vjeroispovijest_id'],
                                             ekonomska_aktivnost_id=data['ekonomska_aktivnost_id'],
                                             bracni_status_id=data['bracni_status_id'],
                                             racunarska_pismenost_id=data['racunarska_pismenost_id'],
                                             obrazovanje_id=data['obrazovanje_id'],
                                             pismenost_id=data['pismenost_id'],
                                             godina_rodjenja=data['godina_rodjenja'], )
        stanovnik.strani_jezici.set(data['strani_jezici'])
        stanovnik.save()
        serializer = StanovnikSerializer(stanovnik, many=False)
        return Response(serializer.data, status=400)


@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def updateOrDeleteStanovnik(request, pk):
    """
    Update or delete the city.
    """

    if request.method == 'PUT':
        data = request.data
        stanovnik = get_object_or_404(Stanovnik, id=pk)
        stanovnik.ime = data['ime']
        stanovnik.grad_id = data['grad_id']
        stanovnik.godina_id = data['godina_id']
        stanovnik.pol_id = data['pol_id']
        stanovnik.drzavljanstvo_id = data['drzavljanstvo_id']
        stanovnik.nacionalnost_id = data['nacionalnost_id']
        stanovnik.jezik_id = data['jezik_id']
        stanovnik.vjeroispovijest_id = data['vjeroispovijest_id']
        stanovnik.ekonomska_aktivnost_id = data['ekonomska_aktivnost_id']
        stanovnik.bracni_status_id = data['bracni_status_id']
        stanovnik.racunarska_pismenost_id = data['racunarska_pismenost_id']
        stanovnik.obrazovanje_id = data['obrazovanje_id']
        stanovnik.pismenost_id = data['pismenost_id']
        stanovnik.godina_rodjenja = data['godina_rodjenja']
        stanovnik.strani_jezici.set(data['strani_jezici'])
        stanovnik.save()
        serializer = StanovnikSerializer(stanovnik, many=False)
        return Response({"message":"Stanovnik uspješno ažuriran","data":serializer.data}, status=200)

    elif request.method == 'DELETE':
        stanovnik = get_object_or_404(Stanovnik, id=pk)
        stanovnik.delete()
        return Response({"message": "Stanovnik uspješno obrisan!"}, status=200)
