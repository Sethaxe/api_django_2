
from django.contrib import admin
from django.urls import path
from pokedex import views
import json

urlpatterns = [
    path('api/items/<int:item_id>/', views.item_request, name='item_request'),
    path('api/items/', views.create_item, name='create_item'),
    path('api/moves/<int:move_id>/', views.move_request, name='move_request'),
    path('api/pokemon/<int:pk>/', views.request_pokemon_by_id, name='get_pokemon_by_id'),
    path('api/pokemon/', views.create_pokemon, name='create_pokemon'),
    path('api/pokemon/<str:name>/', views.pokemon_by_name_request, name='get_pokemon_by_name'),
    path('api/connexion/', views.connect_user, name='connect_user'),
    path('api/user/<int:id>/', views.request_user, name='request_user'),
    path('api/user/', views.create_user, name='create_user'),
    path('api/mesPokemons/', views.request_user_pokemon, name='get_user_pokemons'),
    path('api/role/', views.get_user_role, name='get_user_role'),
]


