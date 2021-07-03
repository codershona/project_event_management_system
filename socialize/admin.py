from django.contrib import admin

from .models import Socialize

# Register your models here.

class SocializeAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    list_filter = ('title',)
    prepopulated_fields = {'slug': ('title', )}



admin.site.register(Socialize, SocializeAdmin)

