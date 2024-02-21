from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views

from .views import CustomTokenObtainPairView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/register/", include("users.urls")),

    path("api/token/", CustomTokenObtainPairView.as_view(), name="token_pair"),
    path("api/token/refresh/", jwt_views.TokenRefreshView.as_view(), name="token_refresh"),

    path("api/v1/records/", include("records.urls")),

    path("api/v1/openai/", include("chatgpt.urls")),

]
