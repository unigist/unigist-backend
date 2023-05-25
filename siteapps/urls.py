from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from siteapps.users.views import (
        get_users_view,
        user_detail,
        auth_user_detail,
        registration_view
    )

from siteapps.posts.views import (
    get_post_detail,
    get_post_list,
)

urlpatterns = [
    # user endpoints
    path('users/', get_users_view, name='get users'),
    path('users/<int:pk>/', user_detail, name='user detail'),
    path('user/account/<int:pk>', auth_user_detail, name="auth user detail"),
    path('auth/login/', obtain_auth_token, name='login token'),
    path('auth/register/', registration_view, name='registration'),

    # post endpoints
    path('posts/', get_post_list, name='post list'),
    path('posts/<str:slug>/', get_post_detail, name='post detail')
]
