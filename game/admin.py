from django.contrib import admin
from .models import Picture
from .models import Topic
from .models import Game

'''
def add_to(modeladmin, request, queryset):
	return 1
add_to.short_description = "Adding"
'''

class PictureAdmin(admin.ModelAdmin):
    list_display = ('word', 'topic' , 'pictureUrl')
    search_fields = ['word', 'topic__topic']
    #actions = [add_to]

class GameAdmin(admin.ModelAdmin):
    exclude = ['current']
    list_display = ('name', 'active', 'number_of_pictures', 'rope_lenght')
    filter_horizontal = ['pictures']


admin.site.register(Picture, PictureAdmin)
admin.site.register(Topic)
admin.site.register(Game, GameAdmin)

