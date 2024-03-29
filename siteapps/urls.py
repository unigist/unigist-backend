from django.urls import path

from siteapps.users.views import (
        get_users_view,
        user_detail,
        auth_user_detail,
        registration_view,
        logic_view

    )

from siteapps.posts.views import (
    auth_post_detail,
    get_post_detail,
    get_articles_list,
    create_post,
)

from siteapps.comments.views import (
    comments_list,
)


urlpatterns = [
    # user endpoints
    path('users/', get_users_view, name='user-list'),
    path('users/<str:public_id>/', user_detail, name='user-detail'),
    path('user/account/<int:pk>', auth_user_detail, name="user-auth-detail"),
    path('auth/login', logic_view, name='user-login'),
    path('auth/register', registration_view, name='user-registration'),

    # post endpoints
    path('posts/', get_articles_list, name='post-list'),
    path('posts/<str:slug>/', get_post_detail, name='post-detail'),
    # handling delete and Put, access by login users
    path('posts/edit/<str:slug>/', auth_post_detail, name='post-update-delete'),
    path('posts/create', create_post, name='post-create'),

    # comments endpoints
    path('comments/', comments_list, name='comments-list'),
]
