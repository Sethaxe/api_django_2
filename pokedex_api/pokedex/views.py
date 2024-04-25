import os
import django
from django.conf import settings
from django.contrib.auth.models import User
from django.urls import path
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import *

@csrf_exempt
def item_request(request, item_id):
    try:
        item = Items.objects.get(id=item_id)
    except Items.DoesNotExist:
        return JsonResponse({'message': 'Item does not exist'}, status=404)

    if request.method == 'GET':
        data = {
            'id': item.id,
            'identifier': item.identifier,
            'category_id': item.category_id,
            'cost': item.cost,
            'fling_power': item.fling_power,
            'fling_effect_id': item.fling_effect_id
        }
        return JsonResponse(data)
    
    elif request.method == 'DELETE':
        try:
            item = Items.objects.get(id=item_id)
            item.delete()
            return JsonResponse({'message': 'Item deleted'}, status=204)
        except Items.DoesNotExist:
            return JsonResponse({'error': 'Item not found'}, status=404)

    else:
        return JsonResponse({'message': 'Unsupported method'}, status=405)


@csrf_exempt
def create_item(request):
    if request.method == 'POST':
        data_post = json.loads(request.body)
        try:
            new_item = Items.objects.create(
                id=data_post['id'],
                identifier=data_post['identifier'],
                category_id=data_post['category_id'],
                cost=data_post['cost'],
                fling_power=data_post.get('fling_power', None),
                fling_effect_id=data_post.get('fling_effect_id', None),
            )
            return JsonResponse({'message': 'Item created', 'id': new_item.id}, status=201)
        except KeyError:
            return JsonResponse({'error': 'Missing key in request data'}, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

def move_request(request, move_id):
    try:
        move = Move.objects.get(id=move_id)
    except Move.DoesNotExist:
        return JsonResponse({'message': 'Move not found'}, status=404)

    if request.method == 'GET':
        data = {
            'id': move.id,
            'identifier': move.identifier,
            'generation_id': move.generation_id,
            'type_id': move.type_id,
            'power': move.power,
            'pp': move.pp,
            'accuracy': move.accuracy,
            'priority': move.priority,
            'target_id': move.target_id,
            'damage_class_id': move.damage_class_id,
            'effect_id': move.effect_id,
            'effect_chance': move.effect_chance,
            'contest_type_id': move.contest_type_id,
            'contest_effect_id': move.contest_effect_id,
            'super_contest_effect_id': move.super_contest_effect_id
        }
        return JsonResponse(data)

def request_pokemon_by_id(request, pk):
    if request.method == 'GET':
        try:
            pokemon = Pokemon.objects.get(id=pk)
            data = {
                'id': pokemon.id,
                'identifier': pokemon.identifier,
                'species_id': pokemon.species_id,
                'height': pokemon.height,
                'weight': pokemon.weight,
                'base_experience': pokemon.base_experience,
                'order': pokemon.order,
                'is_default': pokemon.is_default
            }
            return JsonResponse(data)
        except Pokemon.DoesNotExist:
            return JsonResponse({'error': 'Pokemon not found'}, status=404)

    elif request.method == 'DELETE':
        try:
            pokemon = Pokemon.objects.get(id=pk)
            pokemon.delete()
            return JsonResponse({'message': 'Pokemon deleted'}, status=204)
        except Pokemon.DoesNotExist:
            return JsonResponse({'error': 'Pokemon not found'}, status=404)

@csrf_exempt
def create_pokemon(request):
    if request.method == 'POST':
        data_post = json.loads(request.body)
    
        new_pokemon = Pokemon.objects.create(
            id=data_post['id'],
            identifier=data_post['identifier'],
            species_id=data_post['species_id'],
            height=data_post['height'],
            weight=data_post['weight'],
            base_experience=data_post['base_experience'],
            order=data_post['order'],
            is_default=data_post['is_default']
    )
        return JsonResponse({'message': 'Pokemon created', 'id': new_pokemon.id}, status=201)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

def pokemon_by_name_request(request, name):
    try:
        pokemon = Pokemon.objects.get(identifier=name)
    except Pokemon.DoesNotExist:
        return JsonResponse({'error': 'Pokemon not found'}, status=404)

    if request.method == 'GET':
        data = {
            'id': pokemon.id,
            'identifier': pokemon.identifier,
            'species_id': pokemon.species_id,
            'height': pokemon.height,
            'weight': pokemon.weight,
            'base_experience': pokemon.base_experience,
            'order': pokemon.order,
            'is_default': pokemon.is_default
        }
        return JsonResponse(data)

    elif request.method == 'DELETE':
        try:
            pokemon = Pokemon.objects.get(identifier=name)
            pokemon.delete()
            return JsonResponse({'message': 'Pokemon deleted'}, status=204)
        except Pokemon.DoesNotExist:
            return JsonResponse({'error': 'Pokemon not found'}, status=404)
        
    else:
        return JsonResponse({'message': 'Method not allowed'}, status=405)

def connect_user(request):
    return JsonResponse({'message': 'User connected'})

@csrf_exempt
def request_user(request, id):
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        return JsonResponse({'message': 'User does not exist'}, status=404)
    
    if request.method == 'GET':
        data = {
            'id': user.id,
            'nom': user.nom,
            'prenom': user.prenom,
            'pokemon_id': user.pokemon_id
        }
        return JsonResponse(data)

    elif request.method == 'DELETE':
        user.delete()
        return JsonResponse({'message': 'User deleted'})

    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

@csrf_exempt
def create_user(request):
    if request.method == 'POST':
        data_post = json.loads(request.body)
        try:
            new_user = User.objects.create(
                id=data_post['id'],
                nom=data_post['nom'],
                prenom=data_post['prenom'],
                pokemon_id=data_post['pokemon_id'],
            )
            return JsonResponse({'message': 'User created', 'id': new_user.id}, status=201)
        except KeyError:
            return JsonResponse({'error': 'Missing key in request data'}, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
    
def request_user_pokemon(request):
    user = request.user
    
    if request.method == 'GET':
        user_pokemons = Pokemon.objects.filter(owner=user)
        pokemon_list = [{'id': pokemon.id, 'name': pokemon.name} for pokemon in user_pokemons]
        return JsonResponse({'pokemons': pokemon_list})

    elif request.method == 'POST':
        data_post = request.POST
        new_pokemon = Pokemon.objects.create(
            name=data_post['name'],
            owner=user
        )
        return JsonResponse({'message': 'Pokemon created', 'id': new_pokemon.id}, status=201)

    elif request.method == 'DELETE':
        user_pokemons = Pokemon.objects.filter(owner=user)
        user_pokemons.delete()
        return JsonResponse({'message': 'User pokemons deleted'}, status=204)

    else:
        return JsonResponse({'error': 'Unsupported method'}, status=405)

def get_user_role(request):
    user = request.user
    if user.is_authenticated:
        role = 'admin' if user.is_staff else 'user'
        return JsonResponse({'role': role})
    else:
        return JsonResponse({'error': 'User not authenticated'}, status=401)

