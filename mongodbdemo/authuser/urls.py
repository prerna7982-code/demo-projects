from .views import *
from django.urls import path,include
from django.conf.urls import url
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
	path('register/',RegisterView.as_view()),
    path('update_profile/<int:pk>/', UpdateProfileView.as_view(), name='auth_update_profile'),
    path('users/',UserDetailView.as_view()),
	path('token/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/', LoginApiView.as_view(), name='login'),
    path('logout/', UserLogout.as_view(), name='logout'),
    ]