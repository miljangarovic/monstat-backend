from django.contrib import admin
from django.apps import apps

# Register your models here.
import stanovnici.models

admin.site.register(stanovnici.models.Grad)
admin.site.register(stanovnici.models.Godina)
admin.site.register(stanovnici.models.Pol)
admin.site.register(stanovnici.models.Stanovnik)
admin.site.register(stanovnici.models.Pismenost)
admin.site.register(stanovnici.models.StraniJezik)
admin.site.register(stanovnici.models.StepenObrazovanja)
admin.site.register(stanovnici.models.RacunarksaPismenost)
admin.site.register(stanovnici.models.BracniStatus)
admin.site.register(stanovnici.models.EkonomskaAktivnost)
admin.site.register(stanovnici.models.Nacionalnost)
admin.site.register(stanovnici.models.MaternjiJezik)
admin.site.register(stanovnici.models.Vjeroispovijest)
admin.site.register(stanovnici.models.Drzavljanstvno)
