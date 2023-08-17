# Hier passiert die haupt spielabläufe
from card_Repository import cardRepo
import Player as pl


card_repo = cardRepo()
player1 = pl.player("Player1")
player2 = pl.player("Player2")
card_repo.handout_multiple_cards(6, player1)
card_repo.handout_multiple_cards(6, player2)
