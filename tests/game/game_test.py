from unittest import TestCase

from game.game import Game
from model.player import Player
from model.card import Card


class GameWithThreePlayerTest(TestCase):
    def setUp(self):
        self.game = Game([Player("P1"), Player("P2"), Player("P3")])

    def test_createDeck_correctSize(self):
        # then
        self.assertEquals(len(self.game.card_deck), 32)

    def test_createDeck_containsAllCards(self):
        # then
        self.assertTrue(Card(Card.Suit.BELLS, Card.Face.SEVEN) in self.game.card_deck)
        self.assertTrue(Card(Card.Suit.BELLS, Card.Face.EIGHT) in self.game.card_deck)
        self.assertTrue(Card(Card.Suit.BELLS, Card.Face.NINE) in self.game.card_deck)
        self.assertTrue(Card(Card.Suit.BELLS, Card.Face.TEN) in self.game.card_deck)
        self.assertTrue(Card(Card.Suit.BELLS, Card.Face.JACK) in self.game.card_deck)
        self.assertTrue(Card(Card.Suit.BELLS, Card.Face.QUEEN) in self.game.card_deck)
        self.assertTrue(Card(Card.Suit.BELLS, Card.Face.KING) in self.game.card_deck)
        self.assertTrue(Card(Card.Suit.BELLS, Card.Face.ACE) in self.game.card_deck)

        self.assertTrue(Card(Card.Suit.HEARTS, Card.Face.SEVEN) in self.game.card_deck)
        self.assertTrue(Card(Card.Suit.HEARTS, Card.Face.EIGHT) in self.game.card_deck)
        self.assertTrue(Card(Card.Suit.HEARTS, Card.Face.NINE) in self.game.card_deck)
        self.assertTrue(Card(Card.Suit.HEARTS, Card.Face.TEN) in self.game.card_deck)
        self.assertTrue(Card(Card.Suit.HEARTS, Card.Face.JACK) in self.game.card_deck)
        self.assertTrue(Card(Card.Suit.HEARTS, Card.Face.QUEEN) in self.game.card_deck)
        self.assertTrue(Card(Card.Suit.HEARTS, Card.Face.KING) in self.game.card_deck)
        self.assertTrue(Card(Card.Suit.HEARTS, Card.Face.ACE) in self.game.card_deck)

        self.assertTrue(Card(Card.Suit.LEAVES, Card.Face.SEVEN) in self.game.card_deck)
        self.assertTrue(Card(Card.Suit.LEAVES, Card.Face.EIGHT) in self.game.card_deck)
        self.assertTrue(Card(Card.Suit.LEAVES, Card.Face.NINE) in self.game.card_deck)
        self.assertTrue(Card(Card.Suit.LEAVES, Card.Face.TEN) in self.game.card_deck)
        self.assertTrue(Card(Card.Suit.LEAVES, Card.Face.JACK) in self.game.card_deck)
        self.assertTrue(Card(Card.Suit.LEAVES, Card.Face.QUEEN) in self.game.card_deck)
        self.assertTrue(Card(Card.Suit.LEAVES, Card.Face.KING) in self.game.card_deck)
        self.assertTrue(Card(Card.Suit.LEAVES, Card.Face.ACE) in self.game.card_deck)

        self.assertTrue(Card(Card.Suit.ACORNS, Card.Face.SEVEN) in self.game.card_deck)
        self.assertTrue(Card(Card.Suit.ACORNS, Card.Face.EIGHT) in self.game.card_deck)
        self.assertTrue(Card(Card.Suit.ACORNS, Card.Face.NINE) in self.game.card_deck)
        self.assertTrue(Card(Card.Suit.ACORNS, Card.Face.TEN) in self.game.card_deck)
        self.assertTrue(Card(Card.Suit.ACORNS, Card.Face.JACK) in self.game.card_deck)
        self.assertTrue(Card(Card.Suit.ACORNS, Card.Face.QUEEN) in self.game.card_deck)
        self.assertTrue(Card(Card.Suit.ACORNS, Card.Face.KING) in self.game.card_deck)
        self.assertTrue(Card(Card.Suit.ACORNS, Card.Face.ACE) in self.game.card_deck)

    def test_createDeck_noDuplicateCards(self):
        # given
        card_counter = {}

        for card in self.game.card_deck:
            count = card_counter.get(card, 0)
            card_counter[card] = count + 1

        # then
        for card, count in card_counter.items():
            self.assertEquals(count, 1)

    def test_clearCards(self):
        # given
        self.game.skat.append(Card(Card.Suit.BELLS, Card.Face.SEVEN))
        self.game.players[0].cards.append(Card(Card.Suit.BELLS, Card.Face.EIGHT))
        self.game.players[1].cards.append(Card(Card.Suit.BELLS, Card.Face.NINE))
        self.game.players[2].cards.append(Card(Card.Suit.BELLS, Card.Face.TEN))

        # when
        self.game.clear_cards()

        # then
        self.assertEquals(len(self.game.skat), 0)
        self.assertEquals(len(self.game.players[0].cards), 0)
        self.assertEquals(len(self.game.players[1].cards), 0)
        self.assertEquals(len(self.game.players[2].cards), 0)

    def test_reset_withoutDealer(self):
        # given
        self.game.bid_value = 24
        self.game.dealer = 2
        self.game.skat.append(Card(Card.Suit.BELLS, Card.Face.SEVEN))
        self.game.players[0].cards.append(Card(Card.Suit.BELLS, Card.Face.EIGHT))
        self.game.players[1].cards.append(Card(Card.Suit.BELLS, Card.Face.NINE))
        self.game.players[2].cards.append(Card(Card.Suit.BELLS, Card.Face.TEN))

        # when
        self.game.reset()

        # then
        # clear cards had to be called
        self.assertEquals(len(self.game.skat), 0)
        self.assertEquals(len(self.game.players[0].cards), 0)
        self.assertEquals(len(self.game.players[1].cards), 0)
        self.assertEquals(len(self.game.players[2].cards), 0)
        # reset bid value
        self.assertEquals(self.game.bid_value, -1)
        # reset game variant
        self.assertEquals(self.game.game_variant, None)
        # untouched dealer
        self.assertEquals(self.game.dealer, 2)

    def test_reset_witDealer(self):
        # given
        self.game.bid_value = 24
        self.game.dealer = 2
        self.game.skat.append(Card(Card.Suit.BELLS, Card.Face.SEVEN))
        self.game.players[0].cards.append(Card(Card.Suit.BELLS, Card.Face.EIGHT))
        self.game.players[1].cards.append(Card(Card.Suit.BELLS, Card.Face.NINE))
        self.game.players[2].cards.append(Card(Card.Suit.BELLS, Card.Face.TEN))

        # when
        self.game.reset(True)

        # then
        # cleared cards
        self.assertEquals(len(self.game.skat), 0)
        self.assertEquals(len(self.game.players[0].cards), 0)
        self.assertEquals(len(self.game.players[1].cards), 0)
        self.assertEquals(len(self.game.players[2].cards), 0)
        # reset bid value
        self.assertEquals(self.game.bid_value, -1)
        # reset game variant
        self.assertEquals(self.game.game_variant, None)
        # reset dealer
        self.assertEquals(self.game.dealer, -1)