# jwt authentication
# from .views import registration_view
# from django.urls import path
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


# urlpatterns = [
#     path('register/', registration_view, name='register'),
#     path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
# ]


# --------------------------------------------------------------------------------------------------------------------------------------------
# token authentication
from rest_framework.authtoken.views import obtain_auth_token # this will provide a token once correct username and password are provided
from django.urls import path
from .views import registration_view, logout_view

urlpatterns = [
    path('login/', obtain_auth_token, name='login'),
    path('register/', registration_view, name='register'),
    path('logout/', logout_view, name='logout'),
]