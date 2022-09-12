from django.shortcuts import render, redirect
from .models import Profile, Weapon, Character, Shield, Helm, Chest, Leg, Ring, Amulet, Trinket
from .forms import ProfileForm, CharCreateForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# from .models import Profile, Character
# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def characters_index(request):
    characters = Character.objects.all()
    return render(request, 'characters/index.html', { 'characters': characters })

@login_required
def profiles_index(request):
    profiles = Profile.objects.filter(user=request.user)
    # profiles = Profile.objects.all()
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

@login_required
def profiles_detail(request, profile_id):
    profile = Profile.objects.get(id=profile_id)
    return render(request, 'profiles/detail.html', { 'profile': profile })

@login_required
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

class ProfileCreate(LoginRequiredMixin, CreateView):
    model = Profile
    form_class = ProfileForm
    # fields = '__all__'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ProfileUpdate(LoginRequiredMixin, UpdateView):
    model = Profile
    fields = '__all__'

class ProfileDelete(LoginRequiredMixin, DeleteView):
    model = Profile
    success_url = '/profiles/'

class CharacterCreate(LoginRequiredMixin, CreateView):
    model = Character
    fields = '__all__'
    success_url = '/characters/'

class CharacterUpdate(LoginRequiredMixin, UpdateView):
    model = Character
    fields = '__all__'

class CharacterDelete(LoginRequiredMixin, DeleteView):
    model = Character
    success_url = '/characters/'

def characterCreation(request):
    error_message = ''
    if request.method == 'POST':
        form = CharCreateForm(request.POST)
        print(form)
        if form.is_valid():
            character = form.save()
            print(character)
            return redirect('characters/creation.html')
        else:
            error_message = 'Invalid Character Creation -- Please Try Again'
    form = CharCreateForm()
    context = { 
        'weapons': Weapon.objects.all(),
        'shields': Shield.objects.all(),
        'helmets': Helm.objects.all(),
        'chests': Chest.objects.all(),
        'legs': Leg.objects.all(),
        'rings': Ring.objects.all(),
        'amulets': Amulet.objects.all(),
        'trinkets': Trinket.objects.all(),
        'form': form,
        'error_message': error_message 
        }
    return render(request, 'characters/creation.html', context)


def signup(request):
    error_message = ''
    if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
        # This will add the user to the database
            user = form.save()
            # This is how we log a user in via code
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = { 'form': form, 'error_message': error_message }
    return render(request, 'registration/signup.html', context)
