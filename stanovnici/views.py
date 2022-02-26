from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from .models import Stanovnik, Godina, Drzavljanstvo, MaternjiJezik, Nacionalnost, EkonomskaAktivnost, BracniStatus, \
    RacunarksaPismenost, Vjeroispovijest, StepenObrazovanja, StraniJezik
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from stanovnici.serializers import UserSerializer, StanovnikSerializer, GradSerializer, GodinaSerializer, \
    DrzavljanstvoSerializer, MaternjiJezikSerializer, NacionalnostSerializer, EkonomskaAktivnostSerializer, \
    BracniStatusSerializer, RacunarksaPismenostSerializer, VjeroispovijestSerializer, StepenObrazovanjaSerializer, \
    StraniJezikSerializer
from .models import Grad


@api_view(['GET'])
def getRoutes(request):
    routes = [
        {'GET': '/api/people'},
        {'POST': '/api/people'},
        {'GET': '/api/cities'},
    ]
    return Response(routes)


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
        serializer = GradSerializer(grad, many=False)
        return Response(serializer.data, status=200)


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
        return Response({"message": "Stanovnik uspješno ažuriran", "data": serializer.data}, status=200)

    elif request.method == 'DELETE':
        stanovnik = get_object_or_404(Stanovnik, id=pk)
        stanovnik.delete()
        return Response({"message": "Stanovnik uspješno obrisan!"}, status=200)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def godine(request):
    """
    List all years, or create a new year.
    """

    if request.method == 'GET':
        godine = Godina.objects.all()
        serializer = GodinaSerializer(godine, many=True)
        return Response(serializer.data, status=200)

    elif request.method == 'POST':
        data = request.data
        godina = Godina.objects.create(godina=data['godina'])
        serializer = GodinaSerializer(godina, many=False)
        return Response(serializer.data, status=200)


@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def updateOrDeleteGodina(request, pk):
    """
    Update or delete the year.
    """

    if request.method == 'PUT':
        data = request.data
        godina = get_object_or_404(Godina, id=pk)
        godina.godina = data['godina']
        godina.save()
        serializer = GodinaSerializer(godina, many=False)
        return Response(serializer.data, status=200)

    elif request.method == 'DELETE':
        godina = get_object_or_404(Godina, id=pk)
        godina.delete()
        return Response(status=200)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def drzavljanstva(request):
    """
    List all drzavljanstva, or create a new drzavljanstvo.
    """

    if request.method == 'GET':
        drzavljanstva = Drzavljanstvo.objects.all()
        serializer = DrzavljanstvoSerializer(drzavljanstva, many=True)
        return Response(serializer.data, status=200)

    elif request.method == 'POST':
        data = request.data
        drzavljanstvo = Drzavljanstvo.objects.create(naziv=data['naziv'])
        serializer = DrzavljanstvoSerializer(drzavljanstvo, many=False)
        return Response(serializer.data, status=200)


@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def updateOrDeleteDrzavljanstvo(request, pk):
    """
    Update or delete the drzavljanstvo.
    """

    if request.method == 'PUT':
        data = request.data
        drzavljanstvo = get_object_or_404(Drzavljanstvo, id=pk)
        drzavljanstvo.naziv = data['naziv']
        drzavljanstvo.save()
        serializer = DrzavljanstvoSerializer(drzavljanstvo, many=False)
        return Response(serializer.data, status=200)

    elif request.method == 'DELETE':
        drzavljanstvo = get_object_or_404(Drzavljanstvo, id=pk)
        drzavljanstvo.delete()
        return Response(status=200)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def maternjiJezici(request):
    """
    List all maternjijezici, or create a new MaternjiJezik.
    """

    if request.method == 'GET':
        maternji_jezici = MaternjiJezik.objects.all()
        serializer = MaternjiJezikSerializer(maternji_jezici, many=True)
        return Response(serializer.data, status=200)

    elif request.method == 'POST':
        data = request.data
        maternji_jezik = MaternjiJezik.objects.create(naziv=data['naziv'])
        serializer = MaternjiJezikSerializer(maternji_jezik, many=False)
        return Response(serializer.data, status=200)


@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def updateOrDeleteMaternjiJezik(request, pk):
    """
    Update or delete the MaternjiJezik.
    """

    if request.method == 'PUT':
        data = request.data
        maternji_jezik = get_object_or_404(MaternjiJezik, id=pk)
        maternji_jezik.naziv = data['naziv']
        maternji_jezik.save()
        serializer = MaternjiJezikSerializer(maternji_jezik, many=False)
        return Response(serializer.data, status=200)

    elif request.method == 'DELETE':
        maternji_jezik = get_object_or_404(MaternjiJezik, id=pk)
        maternji_jezik.delete()
        return Response(status=200)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def nacionalnosti(request):
    """
    List all nacionalnosti, or create a new Nacionalnost.
    """

    if request.method == 'GET':
        nacionalnosti = Nacionalnost.objects.all()
        serializer = NacionalnostSerializer(nacionalnosti, many=True)
        return Response(serializer.data, status=200)

    elif request.method == 'POST':
        data = request.data
        nacionalnost = Nacionalnost.objects.create(naziv=data['naziv'])
        serializer = NacionalnostSerializer(nacionalnost, many=False)
        return Response(serializer.data, status=200)


@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def updateOrDeleteNacionalnost(request, pk):
    """
    Update or delete the Nacionalnost.
    """

    if request.method == 'PUT':
        data = request.data
        nacionalnost = get_object_or_404(Nacionalnost, id=pk)
        nacionalnost.naziv = data['naziv']
        nacionalnost.save()
        serializer = NacionalnostSerializer(nacionalnost, many=False)
        return Response(serializer.data, status=200)

    elif request.method == 'DELETE':
        nacionalnost = get_object_or_404(Nacionalnost, id=pk)
        nacionalnost.delete()
        return Response(status=200)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def ekonomskeAktivnosti(request):
    """
    List all ekonomske aktivnosti, or create a new EkonomskaAktivnost.
    """

    if request.method == 'GET':
        ekonomske_aktivnosti = EkonomskaAktivnost.objects.all()
        serializer = EkonomskaAktivnostSerializer(ekonomske_aktivnosti, many=True)
        return Response(serializer.data, status=200)

    elif request.method == 'POST':
        data = request.data
        ekonomska_aktivnost = EkonomskaAktivnost.objects.create(naziv=data['naziv'])
        serializer = EkonomskaAktivnostSerializer(ekonomska_aktivnost, many=False)
        return Response(serializer.data, status=200)


@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def updateOrDeleteEkonomskaAktivnost(request, pk):
    """
    Update or delete the EkonomskaAktivnost.
    """

    if request.method == 'PUT':
        data = request.data
        ekonomska_aktivnost = get_object_or_404(EkonomskaAktivnost, id=pk)
        ekonomska_aktivnost.naziv = data['naziv']
        ekonomska_aktivnost.save()
        serializer = EkonomskaAktivnostSerializer(ekonomska_aktivnost, many=False)
        return Response(serializer.data, status=200)

    elif request.method == 'DELETE':
        ekonomska_aktivnost = get_object_or_404(EkonomskaAktivnost, id=pk)
        ekonomska_aktivnost.delete()
        return Response(status=200)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def bracniStatusi(request):
    """
    List all bracni statusi, or create a new BracniStatus.
    """

    if request.method == 'GET':
        bracni_statusi = BracniStatus.objects.all()
        serializer = BracniStatusSerializer(bracni_statusi, many=True)
        return Response(serializer.data, status=200)

    elif request.method == 'POST':
        data = request.data
        bracni_status = BracniStatus.objects.create(naziv=data['naziv'])
        serializer = BracniStatusSerializer(bracni_status, many=False)
        return Response(serializer.data, status=200)


@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def updateOrDeleteBracniStatus(request, pk):
    """
    Update or delete the BracniStatus.
    """

    if request.method == 'PUT':
        data = request.data
        bracni_status = get_object_or_404(BracniStatus, id=pk)
        bracni_status.naziv = data['naziv']
        bracni_status.save()
        serializer = BracniStatusSerializer(bracni_status, many=False)
        return Response(serializer.data, status=200)

    elif request.method == 'DELETE':
        bracni_status = get_object_or_404(BracniStatus, id=pk)
        bracni_status.delete()
        return Response(status=200)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def racunarskePismenosti(request):
    """
    List all racunarske pismenosti, or create a new RacunarksaPismenost.
    """

    if request.method == 'GET':
        racunarske_pismenosti = RacunarksaPismenost.objects.all()
        serializer = RacunarksaPismenostSerializer(racunarske_pismenosti, many=True)
        return Response(serializer.data, status=200)

    elif request.method == 'POST':
        data = request.data
        racunarska_pismenost = RacunarksaPismenost.objects.create(naziv=data['naziv'])
        serializer = RacunarksaPismenostSerializer(racunarska_pismenost, many=False)
        return Response(serializer.data, status=200)


@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def updateOrDeleteRacunarksaPismenost(request, pk):
    """
    Update or delete the RacunarksaPismenost.
    """

    if request.method == 'PUT':
        data = request.data
        racunarska_pismenost = get_object_or_404(RacunarksaPismenost, id=pk)
        racunarska_pismenost.naziv = data['naziv']
        racunarska_pismenost.save()
        serializer = RacunarksaPismenostSerializer(racunarska_pismenost, many=False)
        return Response(serializer.data, status=200)

    elif request.method == 'DELETE':
        racunarska_pismenost = get_object_or_404(RacunarksaPismenost, id=pk)
        racunarska_pismenost.delete()
        return Response(status=200)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def vjeroispovijesti(request):
    """
    List all vjeroispovijesti, or create a new Vjeroispovijest.
    """

    if request.method == 'GET':
        vjeroispovijesti = Vjeroispovijest.objects.all()
        serializer = VjeroispovijestSerializer(vjeroispovijesti, many=True)
        return Response(serializer.data, status=200)

    elif request.method == 'POST':
        data = request.data
        vjeroispovijest = Vjeroispovijest.objects.create(naziv=data['naziv'])
        serializer = VjeroispovijestSerializer(vjeroispovijest, many=False)
        return Response(serializer.data, status=200)


@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def updateOrDeleteVjeroispovijest(request, pk):
    """
    Update or delete the Vjeroispovijest.
    """

    if request.method == 'PUT':
        data = request.data
        vjeroispovijest = get_object_or_404(Vjeroispovijest, id=pk)
        vjeroispovijest.naziv = data['naziv']
        vjeroispovijest.save()
        serializer = VjeroispovijestSerializer(vjeroispovijest, many=False)
        return Response(serializer.data, status=200)

    elif request.method == 'DELETE':
        vjeroispovijest = get_object_or_404(Vjeroispovijest, id=pk)
        vjeroispovijest.delete()
        return Response(status=200)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def stepeniObrazovanja(request):
    """
    List all stepeni obrazovanja, or create a new StepenObrazovanja.
    """

    if request.method == 'GET':
        stepeni_obrazovanja = StepenObrazovanja.objects.all()
        serializer = StepenObrazovanjaSerializer(stepeni_obrazovanja, many=True)
        return Response(serializer.data, status=200)

    elif request.method == 'POST':
        data = request.data
        stepen_obrazovanja = StepenObrazovanja.objects.create(naziv=data['naziv'])
        serializer = StepenObrazovanjaSerializer(stepen_obrazovanja, many=False)
        return Response(serializer.data, status=200)


@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def updateOrDeleteStepenObrazovanja(request, pk):
    """
    Update or delete the StepenObrazovanja.
    """

    if request.method == 'PUT':
        data = request.data
        stepen_obrazovanja = get_object_or_404(StepenObrazovanja, id=pk)
        stepen_obrazovanja.naziv = data['naziv']
        stepen_obrazovanja.save()
        serializer = StepenObrazovanjaSerializer(stepen_obrazovanja, many=False)
        return Response(serializer.data, status=200)

    elif request.method == 'DELETE':
        stepen_obrazovanja = get_object_or_404(StepenObrazovanja, id=pk)
        stepen_obrazovanja.delete()
        return Response(status=200)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def straniJezik(request):
    """
    List all maternjijezici, or create a new StraniJezik.
    """

    if request.method == 'GET':
        strani_jezici = StraniJezik.objects.all()
        serializer = StraniJezikSerializer(strani_jezici, many=True)
        return Response(serializer.data, status=200)

    elif request.method == 'POST':
        data = request.data
        strani_jezik = StraniJezik.objects.create(naziv=data['naziv'])
        serializer = StraniJezikSerializer(strani_jezik, many=False)
        return Response(serializer.data, status=200)


@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def updateOrDeleteStraniJezik(request, pk):
    """
    Update or delete the StraniJezik.
    """

    if request.method == 'PUT':
        data = request.data
        strani_jezik = get_object_or_404(StraniJezik, id=pk)
        strani_jezik.naziv = data['naziv']
        strani_jezik.save()
        serializer = StraniJezikSerializer(strani_jezik, many=False)
        return Response(serializer.data, status=200)

    elif request.method == 'DELETE':
        strani_jezik = get_object_or_404(StraniJezik, id=pk)
        strani_jezik.delete()
        return Response(status=200)
