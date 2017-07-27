from django import forms
from .models import Game

class GameAdminForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = '__all__'

    def clean_pictures(self):
        pictures = self.cleaned_data.get('pictures')
        if pictures and len(pictures) < 4:
            raise forms.ValidationError("You need minimum 4 pictures to start a game!")
        return pictures
