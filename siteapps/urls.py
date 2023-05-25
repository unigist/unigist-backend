from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from siteapps.users.views import (
        # get_users_view,
        # user_detail,
        # auth_user_detail,
        registration_view
    )

urlpatterns = [
    # path('users/', get_users_view, name='get users'),
    # path('users/<int:pk>/', user_detail, name='user detail'),
    # path('user/account/<int:pk>', auth_user_detail, name="auth user detail"),
    path('auth/login/', obtain_auth_token, name='login token'),
    path('auth/register/', registration_view, name='registration'),
]
