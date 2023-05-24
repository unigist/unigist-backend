from django.urls import path

from siteapps.users.views import get_users_view

urlpatterns = [
    path('users/', get_users_view, name='get users'),
]
