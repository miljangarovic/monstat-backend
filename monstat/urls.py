from django.contrib import admin
from django.urls import include, path
from stanovnici import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.getRoutes),
    path('api/', include('stanovnici.urls')),
    path('api/register',views.registerUser),
    path('api/users',views.getUsers),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
