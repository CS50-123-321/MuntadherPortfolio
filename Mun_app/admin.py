from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
# Register your models here.
#admin username is my username is "muntadher"
from .models import *
 

admin.site.register(Experience)
admin.site.register(Blog)
admin.site.register(Explore)
#admin.site.register(TextManagementSystem)
admin.site.register(Web_Pages)
admin.site.register(TvSeries)
admin.site.register(Achievement)
admin.site.register(Subscribe)

class PostAdmin(admin.ModelAdmin):
    list_display = ('thumbnail_preview',)
    readonly_fields = ('thumbnail_preview',)

    def thumbnail_preview(self, obj):
        return obj.thumbnail_preview

    thumbnail_preview.short_description = 'Thumbnail Preview'
    thumbnail_preview.allow_tags = True

admin.site.register(TextManagementSystem, PostAdmin)