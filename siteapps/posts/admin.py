from django.contrib import admin

from .models import Post

# Register your models here.
class PostModelAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'slug',
        'author',
        'id',
        'date_published'
    )
    # prepopulated_fields = {"slug": ('author','title')}

admin.site.register(Post, PostModelAdmin)
