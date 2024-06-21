# game/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import GameSession

@login_required
def create_game(request):
    game = GameSession.objects.create(player1=request.user)
    return redirect('game:play_game', game_id=game.id)

@login_required
def play_game(request, game_id):
    game = get_object_or_404(GameSession, id=game_id)

    if request.user == game.player1:
        player = 'player1'
    elif game.player2 is None:
        game.player2 = request.user
        game.save()
        player = 'player2'
    elif request.user == game.player2:
        player = 'player2'
    else:
        return HttpResponse('Unauthorized', status=401)

    if request.method == 'POST':
        choice = request.POST['choice']
        if player == 'player1':
            game.player1_choice = choice
        elif player == 'player2':
            game.player2_choice = choice
        game.save()
        
        if game.player1_choice and game.player2_choice:
            game.completed = True
            game.save()
            return redirect('game:game_result', game_id=game.id)

    return render(request, 'game/play_game.html', {'game': game, 'player': player})

@login_required
def game_result(request, game_id):
    game = get_object_or_404(GameSession, id=game_id)
    winner = game.get_winner()
    return render(request, 'game/game_result.html', {'game': game, 'winner': winner})

@login_required
def redirect_after_login(request):
    # Check the next parameter
    next_url = request.GET.get('next')
    if next_url:
        return redirect(next_url)
    
    # Redirect to a default page if no next URL is provided
    return redirect('game:create_game')