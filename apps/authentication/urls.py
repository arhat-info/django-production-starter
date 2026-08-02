from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView
from .views import (
    CustomTokenObtainPairView,
    RegisterView,
    LogoutView,
    UserProfileView,
    ChangePasswordView,
)

urlpatterns = [
    # ── JWT ──────────────────────────────────────────────────────────
    path('token/',          CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/',  TokenRefreshView.as_view(),          name='token_refresh'),
    path('token/verify/',   TokenVerifyView.as_view(),           name='token_verify'),

    # ── Registration & session ────────────────────────────────────────
    path('register/',       RegisterView.as_view(),              name='register'),
    path('logout/',         LogoutView.as_view(),                name='logout'),

    # ── Profile ───────────────────────────────────────────────────────
    path('me/',             UserProfileView.as_view(),           name='user_profile'),
    path('me/password/',    ChangePasswordView.as_view(),        name='change_password'),
]
