from django.contrib import admin
from .models import Post, Blog

class BlogAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'created', )
    search_fields = ('name', )
    list_filter = ('owner', )
    readonly_fields = ('created', 'updated', )

class PostAdmin(admin.ModelAdmin):
    list_display = ('blog','title', 'created', )
    search_fields = ('title', )
    list_filter = ('created','blog', )
    readonly_fields = ('created', 'updated', )

admin.site.register(Post,PostAdmin)
admin.site.register(Blog,BlogAdmin)