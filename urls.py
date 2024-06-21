from django.urls import path
from . import views

app_name = 'game'

urlpatterns = [
    path('create/', views.create_game, name='create_game'),
    path('play/<int:game_id>/', views.play_game, name='play_game'),
    path('result/<int:game_id>/', views.game_result, name='game_result'),
]
