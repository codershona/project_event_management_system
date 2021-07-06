from django.contrib import admin

from .models import Socialize, Location, Group, Contributor

# Register your models here.

class SocializeAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'location', 'date')
    list_filter = ('location', 'group_name', 'date')
    prepopulated_fields = {'slug': ('title', )}



admin.site.register(Socialize, SocializeAdmin)
admin.site.register(Location)
admin.site.register(Group)
admin.site.register(Contributor)
