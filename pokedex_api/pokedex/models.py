from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.db import models

# Vue pour obtenir les détails d'un item
class items(models.Model):
    id = models.AutoField(primary_key=True)
    identifier = models.CharField(max_length=79)
    category_id = models.IntegerField()
    cost = models.IntegerField()
    fling_power = models.IntegerField(null=True, blank=True)
    fling_effect_id = models.IntegerField(null=True, blank=True)

class EggGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    identifier = models.CharField(max_length=79)

class Location(models.Model):
    id = models.IntegerField(primary_key=True)
    region_id = models.IntegerField(default=None, null=True)
    identifier = models.CharField(max_length=79)

class Move(models.Model):
    id = models.IntegerField(primary_key=True)
    identifier = models.CharField(max_length=79)
    generation_id = models.IntegerField()
    type_id = models.IntegerField()
    power = models.SmallIntegerField(default=None, null=True)
    pp = models.SmallIntegerField(default=None, null=True)
    accuracy = models.SmallIntegerField(default=None, null=True)
    priority = models.SmallIntegerField()
    target_id = models.IntegerField()
    damage_class_id = models.IntegerField()
    effect_id = models.IntegerField()
    effect_chance = models.IntegerField(default=None, null=True)
    contest_type_id = models.IntegerField(default=None, null=True)
    contest_effect_id = models.IntegerField(default=None, null=True)
    super_contest_effect_id = models.IntegerField(default=None, null=True)

class Pokemon(models.Model):
    id = models.IntegerField(primary_key=True)
    identifier = models.CharField(max_length=79)
    species_id = models.IntegerField(default=None, null=True)
    height = models.IntegerField()
    weight = models.IntegerField()
    base_experience = models.IntegerField()
    order = models.IntegerField()
    is_default = models.BooleanField()

class PokemonEggGroups(models.Model):
    species_id = models.IntegerField()
    egg_group_id = models.IntegerField()

class PokemonFormGenerations(models.Model):
    pokemon_form_id = models.IntegerField()
    generation_id = models.IntegerField()
    game_index = models.IntegerField()

class PokemonMoves(models.Model):
    pokemon_id = models.IntegerField()
    version_group_id = models.IntegerField()
    move_id = models.IntegerField()
    pokemon_move_method_id = models.IntegerField()
    level = models.IntegerField()
    order = models.IntegerField(default=None, null=True)

class PokemonStats(models.Model):
    pokemon_id = models.IntegerField()
    stat_id = models.IntegerField()
    base_stat = models.IntegerField()
    effort = models.IntegerField()

class PokemonTypes(models.Model):
    pokemon_id = models.IntegerField()
    type_id = models.IntegerField()
    slot = models.IntegerField()

class Stat(models.Model):
    id = models.IntegerField(primary_key=True)
    damage_class_id = models.IntegerField(default=None, null=True)
    identifier = models.CharField(max_length=79)
    is_battle_only = models.BooleanField()
    game_index = models.IntegerField(default=None, null=True)

class Type(models.Model):
    id = models.IntegerField(primary_key=True)
    identifier = models.CharField(max_length=79)
    generation_id = models.IntegerField()
    damage_class_id = models.IntegerField(default=None, null=True)
    
class User(models.Model):
    id = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=40)
    prenom = models.CharField(max_length=40)
    pokemon_id = models.IntegerField()

class pokemon_types(models.Model):
    pokemon_id = models.IntegerField()
    type_id = models.IntegerField()
    slot = models.IntegerField()


