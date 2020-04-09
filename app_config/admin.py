from django.contrib import admin
from .models import SlideBar, Link

# Register your models here.


class LinkAdnin(admin.ModelAdmin):
    list_display = ('name', 'href', 'status', 'weight', 'create_time')
    fields = ('name', 'href', 'status', 'weight')

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(LinkAdnin, self).save_model(request, obj, form, change)


class SliderBarAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_type', 'content', 'create_time')
    fields = ('title', 'display_type', 'content')

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(SliderBarAdmin, self).save_model(request, obj, form, change)


admin.site.register(Link, LinkAdnin)
admin.site.register(SlideBar, SliderBarAdmin)
