from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=24)
    description = models.TextField(max_length=240)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
		# detail is referring to the name of the route
		# path('cats/<int:cat_id>/', views.cats_detail, name="detail"),
        return reverse('detail.profile', kwargs={'profile_id': self.id})

class Weapon(models.Model):
    name = models.CharField(max_length=48)
    type = models.CharField(max_length=48)
    grip = models.CharField(max_length=48)
    attack_type = models.CharField(max_length=48)
    damage_type = models.CharField(max_length=48)
    physical_damage = models.FloatField()
    magical_damage = models.FloatField()
    critical_chance = models.IntegerField()
    critical_damage = models.FloatField()
    dodge = models.IntegerField()
    roll = models.IntegerField()
    img_URL = models.CharField(max_length=48)

    def __str__(self):
        return self.name

class Shield(models.Model):
    name = models.CharField(max_length=48)
    type = models.CharField(max_length=48)
    physical_resistance = models.IntegerField()
    magical_resistance = models.IntegerField()
    physical_damage = models.FloatField()
    magical_damage = models.FloatField()
    critical_chance = models.IntegerField()
    critical_damage = models.FloatField()
    dodge = models.IntegerField()
    roll = models.IntegerField()
    img_URL = models.CharField(max_length=48)

    def __str__(self):
        return self.name

class Helm(models.Model):
    name = models.CharField(max_length=48)
    type = models.CharField(max_length=48)
    physical_resistance = models.IntegerField()
    magical_resistance = models.IntegerField()
    physical_damage = models.FloatField()
    magical_damage = models.FloatField()
    critical_chance = models.IntegerField()
    critical_damage = models.FloatField()
    dodge = models.IntegerField()
    roll = models.IntegerField()
    img_URL = models.CharField(max_length=48)

    def __str__(self):
        return self.name

class Chest(models.Model):
    name = models.CharField(max_length=48)
    type = models.CharField(max_length=48)
    physical_resistance = models.IntegerField()
    magical_resistance = models.IntegerField()
    physical_damage = models.FloatField()
    magical_damage = models.FloatField()
    critical_chance = models.IntegerField()
    critical_damage = models.FloatField()
    dodge = models.IntegerField()
    roll = models.IntegerField()
    img_URL = models.CharField(max_length=48)

    def __str__(self):
        return self.name

class Leg(models.Model):
    name = models.CharField(max_length=48)
    type = models.CharField(max_length=48)
    physical_resistance = models.IntegerField()
    magical_resistance = models.IntegerField()
    physical_damage = models.FloatField()
    magical_damage = models.FloatField()
    critical_chance = models.IntegerField()
    critical_damage = models.FloatField()
    dodge = models.IntegerField()
    roll = models.IntegerField()
    img_URL = models.CharField(max_length=48)

    def __str__(self):
        return self.name

class Ring(models.Model):
    name = models.CharField(max_length=48)
    physical_resistance = models.IntegerField()
    magical_resistance = models.IntegerField()
    physical_damage = models.FloatField()
    magical_damage = models.FloatField()
    critical_chance = models.IntegerField()
    critical_damage = models.FloatField()
    dodge = models.IntegerField()
    roll = models.IntegerField()
    img_URL = models.CharField(max_length=48)

    def __str__(self):
        return self.name

class Amulet(models.Model):
    name = models.CharField(max_length=48)
    physical_resistance = models.IntegerField()
    magical_resistance = models.IntegerField()
    physical_damage = models.FloatField()
    magical_damage = models.FloatField()
    critical_chance = models.IntegerField()
    critical_damage = models.FloatField()
    dodge = models.IntegerField()
    roll = models.IntegerField()
    img_URL = models.CharField(max_length=48)

    def __str__(self):
        return self.name

class Trinket(models.Model):
    name = models.CharField(max_length=48)
    type = models.CharField(max_length=48)
    physical_resistance = models.IntegerField()
    magical_resistance = models.IntegerField()
    physical_damage = models.FloatField()
    magical_damage = models.FloatField()
    critical_chance = models.IntegerField()
    critical_damage = models.FloatField()
    dodge = models.IntegerField()
    roll = models.IntegerField()
    img_URL = models.CharField(max_length=48)

    def __str__(self):
        return self.name

# FAITHS = (
#     (None, 'Without'),
#     ('Adherent', 'Ancients'),
#     ('Devoted', 'Daethos')
# )
# character model trait
# faith = models.CharField(
#   max_length=10,
#   choices=FAITHS,
#   default=FAITHS[0][0])

class Character(models.Model):
    name = models.CharField(max_length=24)
    description = models.TextField(max_length=240)
    constitution = models.PositiveSmallIntegerField()
    strength = models.PositiveSmallIntegerField()
    dexterity = models.PositiveSmallIntegerField()
    achre = models.PositiveSmallIntegerField()
    caer = models.PositiveSmallIntegerField()
    # weapon_one = models.Weapon.get(id=weapon_id)
    weapon_one = models.ManyToManyField(Weapon, related_name='weapon_one')
    weapon_two = models.ManyToManyField(Weapon, related_name='weapon_two')
    shield = models.ManyToManyField(Shield)
    helm = models.ManyToManyField(Helm)
    chest = models.ManyToManyField(Chest)
    legs = models.ManyToManyField(Leg)
    ring_one = models.ManyToManyField(Ring, related_name='ring_one')
    ring_two = models.ManyToManyField(Ring, related_name='ring_two')
    amulet = models.ManyToManyField(Amulet)
    trinket = models.ManyToManyField(Trinket)
    profile = models.ManyToManyField(Profile)
    adherent = models.BooleanField()
    devoted = models.BooleanField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("detail", kwargs={"character_id": self.id})
    