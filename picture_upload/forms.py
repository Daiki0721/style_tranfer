import os
from django import forms
from .models import PictureUpload

class PictureUploadForm(forms.ModelForm):
    class Meta:
        model = PictureUpload
        fields = ('image',)