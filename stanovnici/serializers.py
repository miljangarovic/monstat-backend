from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Stanovnik, Grad, Godina, Drzavljanstvno, Pol, Vjeroispovijest, MaternjiJezik, Nacionalnost, \
    EkonomskaAktivnost, BracniStatus, RacunarksaPismenost, StepenObrazovanja, StraniJezik, Pismenost


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class GradSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grad
        exclude = []

class GodinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Godina
        exclude = []

class PolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pol
        exclude = []

class DrzavljanstvnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drzavljanstvno
        exclude = []

class MaternjiJezikSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaternjiJezik
        exclude = []

class NacionalnostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nacionalnost
        exclude = []

class EkonomskaAktivnostSerializer(serializers.ModelSerializer):
    class Meta:
        model = EkonomskaAktivnost
        exclude = []

class BracniStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = BracniStatus
        exclude = []

class RacunarksaPismenostSerializer(serializers.ModelSerializer):
    class Meta:
        model = RacunarksaPismenost
        exclude = []

class VjeroispovijestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vjeroispovijest
        exclude = []

class StepenObrazovanjaSerializer(serializers.ModelSerializer):
    class Meta:
        model = StepenObrazovanja
        exclude = []

class StraniJezikSerializer(serializers.ModelSerializer):
    class Meta:
        model = StraniJezik
        exclude = []

class PismenostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pismenost
        exclude = []


class StanovnikSerializer(serializers.ModelSerializer):

    grad_id = GradSerializer()
    godina_id = GodinaSerializer()
    pol_id = PolSerializer()
    drzavljanstvo_id = DrzavljanstvnoSerializer()
    vjeroispovijest_id = VjeroispovijestSerializer()
    jezik_id = MaternjiJezikSerializer()
    nacionalnost_id = NacionalnostSerializer()
    ekonomska_aktivnost_id = EkonomskaAktivnostSerializer()
    bracni_status_id = BracniStatusSerializer()
    racunarska_pismenost_id = RacunarksaPismenostSerializer()
    obrazovanje_id = StepenObrazovanjaSerializer()
    pismenost_id = PismenostSerializer()
    strani_jezici = StraniJezikSerializer(many=True)

    class Meta:
        model = Stanovnik
        exclude = []



