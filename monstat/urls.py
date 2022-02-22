from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from stanovnici import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'stanovnici', views.StanovnikViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api',include('stanovnici.urls')),

    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
