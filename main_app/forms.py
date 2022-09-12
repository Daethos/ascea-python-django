from django import forms
from django.forms import ModelForm
from .models import Character, Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        models = Profile
        fields = ('name', 'description')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }

class CharCreateForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = '__all__'