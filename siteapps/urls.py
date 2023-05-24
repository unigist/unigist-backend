from django.urls import path

from siteapps.users.views import (
        get_users_view,
        get_user_details,
        registration_view
    )

urlpatterns = [
    path('users/', get_users_view, name='get users'),
    path('users/<int:pk>/', get_user_details, name='details users'),
    path('auth/register/', registration_view, name='registration end')
]
