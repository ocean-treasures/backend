from django.contrib import admin
from .models import Picture
from .models import Progress
from .models import Game

class PictureAdmin(admin.ModelAdmin):
    list_display = ('word', 'pictureUrl')

class ProgressAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'max_progress', 'rope_lenght')

class GameAdmin(admin.ModelAdmin):
    list_display = ('name', 'rope_lenght')


admin.site.register(Picture, PictureAdmin)
admin.site.register(Progress, ProgressAdmin)
admin.site.register(Game, GameAdmin)

