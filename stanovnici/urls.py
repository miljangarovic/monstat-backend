from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('stanovnici', views.stanovnici),
    path('stanovnici/<int:pk>', views.updateOrDeleteStanovnik),

    path('gradovi', views.gradovi),
    path('gradovi/<int:pk>', views.updateOrDeleteGrad),

    path('godine', views.godine),
    path('godine/<int:pk>', views.updateOrDeleteGodina),

    path('drzavljanstva', views.drzavljanstva),
    path('drzavljanstva/<int:pk>', views.updateOrDeleteDrzavljanstvo),

    path('maternji-jezici', views.maternjiJezici),
    path('maternji-jezici/<int:pk>', views.updateOrDeleteMaternjiJezik),

    path('strani-jezici', views.straniJezik),
    path('strani-jezici/<int:pk>', views.updateOrDeleteStraniJezik),

    path('stepeni-obrazovanja', views.stepeniObrazovanja),
    path('stepeni-obrazovanja/<int:pk>', views.updateOrDeleteStepenObrazovanja),

    path('racunarske-pismenosti', views.racunarskePismenosti),
    path('racunarske-pismenosti/<int:pk>', views.updateOrDeleteRacunarksaPismenost),

    path('vjeroispovijesti', views.vjeroispovijesti),
    path('vjeroispovijesti/<int:pk>', views.updateOrDeleteVjeroispovijest),

    path('stepeni-obrazovanja', views.stepeniObrazovanja),
    path('strani-jezici/<int:pk>', views.updateOrDeleteStepenObrazovanja),

    path('bracni-statusi', views.bracniStatusi),
    path('bracni-statusi/<int:pk>', views.updateOrDeleteBracniStatus),

    path('statistika/ukupno',views.ukupno),
]
