from django import forms
from django.forms import ModelForm
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        models = Profile
        fields = ('name', 'description')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }