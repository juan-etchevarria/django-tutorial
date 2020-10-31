from django.contrib import admin
from apps.blog.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'updated', 'publish', 'user')
    list_filter = ['title', 'publish', 'user']
    search_fields = ['title', 'publish', 'user']


admin.site.register(Post, PostAdmin)
