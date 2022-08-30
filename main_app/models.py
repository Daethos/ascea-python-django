from django.db import models
from django.urls import reverse

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=24)
    description = models.TextField(max_length=240)

    def __str__(self):
        return self.name

class Weapon(models.Model):
    name = models.CharField(max_length=48)
    type = models.CharField(max_length=48)
    grip = models.CharField(max_length=48)
    attack_type = models.CharField(max_length=48)
    damage_type = models.CharField(max_length=48)
    physical_damage = models.IntegerField()
    magical_damage = models.IntegerField()
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
    physical_damage = models.IntegerField()
    magical_damage = models.IntegerField()
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
    physical_damage = models.IntegerField()
    magical_damage = models.IntegerField()
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
    physical_damage = models.IntegerField()
    magical_damage = models.IntegerField()
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
    physical_damage = models.IntegerField()
    magical_damage = models.IntegerField()
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
    physical_damage = models.IntegerField()
    magical_damage = models.IntegerField()
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
    physical_damage = models.IntegerField()
    magical_damage = models.IntegerField()
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
    physical_damage = models.IntegerField()
    magical_damage = models.IntegerField()
    critical_chance = models.IntegerField()
    critical_damage = models.FloatField()
    dodge = models.IntegerField()
    roll = models.IntegerField()
    img_URL = models.CharField(max_length=48)

    def __str__(self):
        return self.name

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
    