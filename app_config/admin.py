from django.contrib import admin
from .models import SlideBar, Link
from app_blog.admin import BaseOwnerAdmin
from BlogProject.custom_site import custom_site

# Register your models here.


class LinkAdnin(BaseOwnerAdmin):
    list_display = ('name', 'href', 'status', 'weight', 'create_time')
    fields = ('name', 'href', 'status', 'weight')


class SliderBarAdmin(BaseOwnerAdmin):
    list_display = ('title', 'display_type', 'content', 'create_time')
    fields = ('title', 'display_type', 'content')


custom_site.register(Link, LinkAdnin)
custom_site.register(SlideBar, SliderBarAdmin)
