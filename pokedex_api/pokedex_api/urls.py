
from django.contrib import admin
from django.urls import path
from pokedex import views
import json

urlpatterns = [
    path('api/items/<int:item_id>/', views.get_item, name='get_item'),
    path('api/moves/<int:move_id>/', views.get_move, name='get_move'),
    path('api/pokemon/<int:pk>/', views.get_pokemon_by_id, name='get_pokemon_by_id'),
    path('api/pokemon/<str:name>/', views.get_pokemon_by_name, name='get_pokemon_by_name'),
    path('api/pokemon/types/<str:pokemon_type>/', views.get_pokemon_by_type, name='get_pokemon_by_type'),
    path('api/connexion/', views.connect_user, name='connect_user'),
    path('api/register/', views.register_user, name='register_user'),
    path('api/mesPokemons/', views.get_user_pokemons, name='get_user_pokemons'),
    path('api/role/', views.get_user_role, name='get_user_role'),
]


