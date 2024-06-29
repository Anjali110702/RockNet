# game/models.py
from django.db import models
from django.contrib.auth.models import User



class GameSession(models.Model):
    player1 = models.ForeignKey(User, related_name='player1', on_delete=models.CASCADE)
    player2 = models.ForeignKey(User, related_name='player2', null=True, blank=True, on_delete=models.CASCADE)
    player1_choice = models.CharField(max_length=10, null=True, blank=True)
    player2_choice = models.CharField(max_length=10, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    def get_winner(self):
        if self.player1_choice and self.player2_choice:
            if self.player1_choice == self.player2_choice:
                return "Draw"
            if (self.player1_choice == 'rock' and self.player2_choice == 'scissors') or \
               (self.player1_choice == 'scissors' and self.player2_choice == 'paper') or \
               (self.player1_choice == 'paper' and self.player2_choice == 'rock'):
                return self.player1
            else:
                return self.player2
        return None
