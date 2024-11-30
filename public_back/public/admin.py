from django.contrib import admin
from .models import Public, Comment

admin.site.register(Public)
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('public', 'stars')