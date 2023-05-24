from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User

# Register your models here.
class UserModelAdmin(UserAdmin):
    list_display = (
        'username', # linkable on the admin panel
        'first_name',
        'last_name',
        'email',
        'is_admin',
        'created',
    )
    search_fields = ('email', 'username')
    readonly_fields = ('id', 'email',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

# Register the User with the UserModelAdmin config
admin.site.register(User, UserModelAdmin)
