from django.urls import path

from users.apps import UsersConfig
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from users.views import UserListAPIView, UserRetrieveAPIView, UserUpdateAPIView, \
    UserDestroyAPIView, UserRegistrationView

app_name = UsersConfig.name

urlpatterns = [
    path('', UserListAPIView.as_view(), name='user_list'),
    path('user_register/', UserRegistrationView.as_view(), name='user_register'),
    path('user/<int:pk>/', UserRetrieveAPIView.as_view(), name='user_detail'),
    path('user/update/<int:pk>/', UserUpdateAPIView.as_view(), name='user_change'),
    path('user/delete/<int:pk>/', UserDestroyAPIView.as_view(), name='user_delete'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

