from django.urls import path
from .views import registration_view, get_profile
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path("register/", registration_view, name="register"),
    path("profile/", get_profile, name="profile"),
    path(
        "auth/token", jwt_views.TokenObtainPairView.as_view(), name="token_obtain_pair"
    ),
    path(
        "auth/token/refresh",
        jwt_views.TokenRefreshView.as_view(),
        name="token_refresh",
    ),
    path(
        "auth/token/revoke", jwt_views.TokenBlacklistView.as_view(), name="auth_logout"
    ),
]
