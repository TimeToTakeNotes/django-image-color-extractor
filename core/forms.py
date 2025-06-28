from django import forms
from .models import ImageColor

# Creates a form letting usrs upload img by exposing only img field from model:
class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageColor
        fields = ['image']