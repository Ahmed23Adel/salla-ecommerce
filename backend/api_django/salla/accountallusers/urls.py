from django.urls import path
from .views import RegisterView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from django.urls import path, include
from .views import *




urlpatterns = [
        path('register/', RegisterView.as_view(), name="sign_up"),
        path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
        path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
        path('verify/', TokenVerifyView.as_view(), name='token_refresh'),
        path('email-verification/<str:id>', VerfiyUserAccount.as_view()),
]

    