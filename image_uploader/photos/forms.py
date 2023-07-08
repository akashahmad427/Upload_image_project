from django import forms
from .models import Images
class Newform(forms.ModelForm):
    class Meta:
        model = Images
        fields = '__all__'
        labels = {'photo':''}