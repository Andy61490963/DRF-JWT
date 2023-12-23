from django.urls import path
from . import views
from .views import DrinkView, DrinkDetailView, LoginView
from rest_framework_simplejwt import views as jwt_views
from rest_framework_simplejwt.views import TokenVerifyView

urlpatterns = [
    path('drinks', DrinkView.as_view(), name='drink'),
    path('drinks/<int:id>', DrinkDetailView.as_view(), name='drink_detail'),
    path('api/login/', LoginView.as_view(), name='login'),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]