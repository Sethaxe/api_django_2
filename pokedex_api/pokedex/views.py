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

@api_view(['GET'])
def get_item(request,item_id):
    item = items.objects.get(id=item_id)
    data = { 'id': item.id, 'name': item.name}
    return JsonResponse(data)

@api_view(['GET'])
def get_move(request, move_id):
    move = Move.objects.get(id=move_id)
    data = {'id': move.id, 'name': move.name}  
    return JsonResponse(data)

@api_view(['GET'])
def get_pokemon_by_id(request, pk):
    try:
        pokemon = pokemon.objects.get(id=pk)
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
    except pokemon.DoesNotExist:
        return JsonResponse({'error': 'Pokemon not found'}, status=404)

@api_view(['GET'])
def get_pokemon_by_name(request, name):
    try:
        pokemon = pokemon.objects.get(identifier=name)
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
    except pokemon.DoesNotExist:
        return JsonResponse({'error': 'Pokemon not found'}, status=404)

def get_pokemon_by_type(request, pokemon_type):
    try:
        pokemon_type_obj = pokemon_types.objects.filter(type_id__identifier=pokemon_type)
        pokemon_list = []
        for obj in pokemon_type_obj:
            pokemon = {
                'pokemon_id': obj.pokemon_id,
                'type_id': obj.type_id.id,
                'slot': obj.slot
            }
            pokemon_list.append(pokemon)
        return JsonResponse({'pokemon_list': pokemon_list})
    except pokemon_types.DoesNotExist:
        return JsonResponse({'error': 'Pokemon type not found'}, status=404)

@api_view(['POST'])
def connect_user(request):
    return JsonResponse({'message': 'User connected'})

@api_view(['POST'])
def register_user(request):
    return JsonResponse({'message': 'User registered'})

@api_view(['GET'])
def get_user_pokemons(request):
    user = request.user
    user_pokemons = Pokemon.objects.filter(owner=user)
    pokemon_list = [{'id': pokemon.id, 'name': pokemon.name} for pokemon in user_pokemons]
    return JsonResponse({'pokemons': pokemon_list})

@api_view(['GET'])
def get_user_role(request):
    user = request.user
    if user.is_authenticated:
        role = 'admin' if user.is_staff else 'user'
        return JsonResponse({'role': role})
    else:
        return JsonResponse({'error': 'User not authenticated'}, status=401)

