from django.contrib import admin
from .models import Picture
from .models import Progress


class PictureAdmin(admin.ModelAdmin):
    list_display = ('word', 'pictureUrl')

class ProgressAdmin(admin.ModelAdmin):
    list_display = ('curr', 'max_progress', 'rope_lenght')


admin.site.register(Picture, PictureAdmin)
admin.site.register(Progress, ProgressAdmin)

