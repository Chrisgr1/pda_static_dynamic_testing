import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card1 = Card("Hearts", 10)
        self.card2 = Card("Spades", 1)
        self.cards = [self.card1, self.card2]
        self.card_game = CardGame()


    def test_card_can_check_for_ace__not_ace(self):
        self.assertEqual(False, self.card_game.check_for_ace(self.card1))

    def test_card_can_highest_card__card_1(self):
        self.assertEqual(self.card1, self.card_game.highest_card(self.card1, self.card2))
        
    def test_cards_can_total(self):
        self.assertEqual("You have a total of 11", self.card_game.cards_total(self.cards))

