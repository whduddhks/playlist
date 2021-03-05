from django import forms
from .models import Myplaylist

class MyplaylistForm(forms.ModelForm):
    class Meta:
        model = Myplaylist
        fields = ['title', 'body', 'list_type', 'list_genre', 'list_play', 'list_image']