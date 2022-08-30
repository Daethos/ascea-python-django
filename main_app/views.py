from django.shortcuts import render
from .models import Profile, Weapon, Character, Shield, Helm, Chest, Leg, Ring, Amulet, Trinket
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# from .models import Profile, Character
# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def characters_index(request):
    characters = Character.objects.all()
    return render(request, 'characters/index.html', { 'characters': characters })

def profiles_index(request):
    profiles = Profile.objects.all()
    return render(request, 'profiles/index.html', { 'profiles': profiles })

def weapons_index(request):
    weapons = Weapon.objects.all()
    return render(request, 'weapons/index.html', { 'weapons': weapons })

def shields_index(request):
    shields = Shield.objects.all()
    return render(request, 'shields/index.html', { 'shields': shields })

def helmets_index(request):
    helmets = Helm.objects.all()
    return render(request, 'helmets/index.html', { 'helmets': helmets })

def chests_index(request):
    chests = Chest.objects.all()
    return render(request, 'chests/index.html', { 'chests': chests })

def legs_index(request):
    legs = Leg.objects.all()
    return render(request, 'legs/index.html', { 'legs': legs })

def rings_index(request):
    rings = Ring.objects.all()
    return render(request, 'rings/index.html', { 'rings': rings })

def amulets_index(request):
    amulets = Amulet.objects.all()
    return render(request, 'amulets/index.html', { 'amulets': amulets })

def trinkets_index(request):
    trinkets = Trinket.objects.all()
    return render(request, 'trinkets/index.html', { 'trinkets': trinkets })

def weapons_detail(request, weapon_id):
    weapon = Weapon.objects.get(id=weapon_id)
    return render(request, 'weapons/detail.html', { 'weapon': weapon })

def shields_detail(request, shield_id):
    shield = Shield.objects.get(id=shield_id)
    return render(request, 'shields/detail.html', { 'shield': shield })

def profiles_detail(request, profile_id):
    profile = Profile.objects.get(id=profile_id)
    return render(request, 'profiles/detail.html', { 'profile': profile })

def characters_detail(request, character_id):
    character = Character.objects.get(id=character_id)
    return render(request, 'characters/detail.html', { 'character': character })

def helmets_detail(request, helm_id):
    helm = Helm.objects.get(id=helm_id)
    return render(request, 'helmets/detail.html', { 'helm': helm })

def chests_detail(request, chest_id):
    chest = Chest.objects.get(id=chest_id)
    return render(request, 'chests/detail.html', { 'chest': chest })

def legs_detail(request, legs_id):
    legs = Leg.objects.get(id=legs_id)
    return render(request, 'legs/detail.html', { 'legs': legs })

def rings_detail(request, ring_id):
    ring = Ring.objects.get(id=ring_id)
    return render(request, 'rings/detail.html', { 'ring': ring })

def amulets_detail(request, amulet_id):
    amulet = Amulet.objects.get(id=amulet_id)
    return render(request, 'amulets/detail.html', { 'amulet': amulet })

def trinkets_detail(request, trinket_id):
    trinket = Trinket.objects.get(id=trinket_id)
    return render(request, 'trinkets/detail.html', { 'trinket': trinket })

class ProfileCreate(CreateView):
    model = Profile
    fields = '__all__'
    success_url = '/profiles/'

class ProfileUpdate(UpdateView):
    model = Profile
    fields = '__all__'

class ProfileDelete(DeleteView):
    model = Profile
    success_url = '/profiles/'

class CharacterCreate(CreateView):
    model = Character
    fields = '__all__'
    success_url = '/characters/'

class CharacterUpdate(UpdateView):
    model = Character
    fields = '__all__'

class CharacterDelete(DeleteView):
    model = Character
    success_url = '/characters/'