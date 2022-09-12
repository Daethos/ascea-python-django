from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('characters/', views.characters_index, name='index.character'),
    path('profiles/', views.profiles_index, name='index.profile'),
    path('weapons/', views.weapons_index, name='index.weapon'),
    path('shields/', views.shields_index, name='index.shield'),
    path('helmets/', views.helmets_index, name='index.helm'),
    path('chests/', views.chests_index, name='index.chest'),
    path('legs/', views.legs_index, name='index.leg'),
    path('rings/', views.rings_index, name='index.ring'),
    path('amulets/', views.amulets_index, name='index.amulet'),
    path('trinkets/', views.trinkets_index, name='index.trinket'),
    path('characters/<int:character_id>/', views.characters_detail, name='detail.character'),
    path('weapons/<int:weapon_id>/', views.weapons_detail, name='detail.weapon'),
    path('shields/<int:shield_id>/', views.shields_detail, name='detail.shield'),
    path('helmets/<int:helm_id>/', views.helmets_detail, name='detail.helm'),
    path('chests/<int:chest_id>/', views.chests_detail, name='detail.chest'),
    path('legs/<int:leg_id>/', views.legs_detail, name='detail.leg'),
    path('rings/<int:ring_id>/', views.rings_detail, name='detail.ring'),
    path('amulets/<int:amulet_id>/', views.amulets_detail, name='detail.amulet'),
    path('trinkets/<int:trinket_id>/', views.trinkets_detail, name='detail.trinket'),
    path('profiles/<int:profile_id>/', views.profiles_detail, name='detail.profile'),
    path('profiles/create/', views.ProfileCreate.as_view(), name='profiles_create'),
    path('profiles/<int:pk>/update', views.ProfileUpdate.as_view(), name='profiles_update'),
    path('profiles/<int:pk>/delete', views.ProfileDelete.as_view(), name='profiles_delete'),
    path('characters/create/', views.CharacterCreate.as_view(), name='characters_create'),
    path('characters/<int:pk>/update', views.CharacterUpdate.as_view(), name='characters_update'),
    path('characters/<int:pk>/delete', views.CharacterDelete.as_view(), name='characters_delete'),
    path('accounts/signup/', views.signup, name='signup'),
    path('characters/creation/', views.characterCreation, name='characterCreation')
]

