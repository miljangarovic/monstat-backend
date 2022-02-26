from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Stanovnik, Grad, Godina, Drzavljanstvno, Pol, Vjeroispovijest, MaternjiJezik, Nacionalnost, \
    EkonomskaAktivnost, BracniStatus, RacunarksaPismenost, StepenObrazovanja, StraniJezik, Pismenost


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'groups']


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
    grad = GradSerializer()
    godina = GodinaSerializer()
    pol = PolSerializer()
    drzavljanstvo = DrzavljanstvnoSerializer()
    vjeroispovijest = VjeroispovijestSerializer()
    jezik = MaternjiJezikSerializer()
    nacionalnost = NacionalnostSerializer()
    ekonomska_aktivnost = EkonomskaAktivnostSerializer()
    bracni_status = BracniStatusSerializer()
    racunarska_pismenost = RacunarksaPismenostSerializer()
    obrazovanje = StepenObrazovanjaSerializer()
    pismenost = PismenostSerializer()
    strani_jezici = StraniJezikSerializer(many=True)
    broj_stranih_jezika = serializers.SerializerMethodField()

    class Meta:
        model = Stanovnik
        fields = '__all__'

    def get_broj_stranih_jezika(self,object):
        strani_jezici = object.strani_jezici
        serializer = StraniJezikSerializer(strani_jezici,many=True)
        return len(serializer.data)



