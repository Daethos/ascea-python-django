from .models import Profile, Character
# from django.contrib.auth.models import User

def add_profiles(request):
    profiles = Profile.objects.all()
    return { 'profiles': profiles, }

def add_characters(request):
    characters = Character.objects.all()
    return { 'characters': characters }