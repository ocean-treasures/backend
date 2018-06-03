from django.contrib import admin
from .forms import GameAdminForm
from .models import Word, Topic, Game


class WordAdmin(admin.ModelAdmin):
    list_display = ('text', 'topic', 'picture_url')
    search_fields = ['text', 'topic__topic']


class GameAdmin(admin.ModelAdmin):
    exclude = ['guessed_words']
    list_display = ('name', 'is_active', 'number_of_pictures', 'rope_lenght')
    filter_horizontal = ['words']

    form = GameAdminForm


admin.site.register(Word, WordAdmin)
admin.site.register(Topic)
admin.site.register(Game, GameAdmin)
