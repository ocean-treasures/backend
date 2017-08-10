from django.contrib import admin

from .forms import GameAdminForm
from .models import Picture, Topic, Game


class PictureAdmin(admin.ModelAdmin):
    list_display = ('word', 'topic', 'pictureUrl')
    search_fields = ['word', 'topic__topic']


class GameAdmin(admin.ModelAdmin):
    exclude = ['current']
    list_display = ('name', 'active', 'number_of_pictures', )
    filter_horizontal = ['pictures']

    form = GameAdminForm


admin.site.register(Picture, PictureAdmin)
admin.site.register(Topic)
admin.site.register(Game, GameAdmin)
