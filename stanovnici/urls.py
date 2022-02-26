from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('cities', views.gradovi),
    path('cities/<int:pk>', views.updateOrDeleteGrad),
    path('people', views.stanovnici),
    path('people/<int:pk>', views.updateOrDeleteStanovnik),

]
