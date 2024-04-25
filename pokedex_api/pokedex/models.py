from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.db import models

class Items(models.Model):
    id = models.IntegerField(primary_key=True)
    identifier = models.CharField(max_length=79)
    category_id = models.IntegerField()
    cost = models.IntegerField()
    fling_power = models.IntegerField(blank=True, null=True)
    fling_effect_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'items'

class EggGroups(models.Model):
    id = models.IntegerField(primary_key=True)
    identifier = models.CharField(max_length=79)

    class Meta:
        managed = False
        db_table = 'egg_groups'

class Location(models.Model):
    id = models.IntegerField(primary_key=True)
    region_id = models.IntegerField(default=None, null=True)
    identifier = models.CharField(max_length=79)
    
    class Meta:
        managed = False
        db_table = 'locations'

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

    class Meta:
        managed = False
        db_table = 'moves'

class Pokemon(models.Model):
    id = models.IntegerField(primary_key=True)
    identifier = models.CharField(max_length=79)
    species_id = models.IntegerField(blank=True, null=True)
    height = models.IntegerField()
    weight = models.IntegerField()
    base_experience = models.IntegerField()
    order = models.IntegerField()
    is_default = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pokemon'

class PokemonEggGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    species_id = models.IntegerField()
    egg_group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pokemon_egg_groups'

class PokemonFormGenerations(models.Model):
    id = models.BigAutoField(primary_key=True)
    pokemon_form_id = models.IntegerField()
    generation_id = models.IntegerField()
    game_index = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pokemon_form_generations'

class PokemonMoves(models.Model):
    id = models.BigAutoField(primary_key=True)
    pokemon_id = models.IntegerField()
    version_group_id = models.IntegerField()
    move_id = models.IntegerField()
    pokemon_move_method_id = models.IntegerField()
    level = models.IntegerField()
    order = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pokemon_moves'

class PokemonStats(models.Model):
    id = models.BigAutoField(primary_key=True)
    pokemon_id = models.IntegerField()
    stat_id = models.IntegerField()
    base_stat = models.IntegerField()
    effort = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pokemon_stats'

class PokemonTypes(models.Model):
    id = models.BigAutoField(primary_key=True)
    pokemon_id = models.IntegerField()
    type_id = models.IntegerField()
    slot = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pokemon_types'

class Stats(models.Model):
    id = models.IntegerField(primary_key=True)
    damage_class_id = models.IntegerField(blank=True, null=True)
    identifier = models.CharField(max_length=79)
    is_battle_only = models.IntegerField()
    game_index = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stat'

class Types(models.Model):
    id = models.IntegerField(primary_key=True)
    identifier = models.CharField(max_length=79)
    generation_id = models.IntegerField()
    damage_class_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'types'
    
class User(models.Model):
    id = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=40)
    prenom = models.CharField(max_length=40)
    pokemon_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user'

