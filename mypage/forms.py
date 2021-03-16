
from django import forms
from .models import Photo

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('image', 'content', )

class Photo(models.Model):
    image = models.ImageField(upload_to='%Y/%m/%d/orig')

class PhotoForm(forms.Form):
    image = forms.ImageField()
