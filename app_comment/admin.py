from django.contrib import admin
from .models import Comment

# Register your models here.


class CommentAdmin(admin.ModelAdmin):
    list_display = ('target', 'nickname', 'content','website','create_time')


admin.site.register(Comment, CommentAdmin)