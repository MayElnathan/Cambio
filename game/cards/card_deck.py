import random

from .card import Card
from .enums import Suit, CardValue

class CardDeck:
    cards: list[Card]

    def __init__(self, number_of_decks: int = 1) -> None:
        for _ in range(number_of_decks):
            normal_card_suits = [Suit.HEARTS, Suit.DIAMONDS, Suit.CLUBS, Suit.SPADES]
            joker_suits = [Suit.RED_JOKER, Suit.BLACK_JOKER]
            self.cards = [Card(value, suit) for suit in normal_card_suits for value in CardValue if value != CardValue.JOKER]
            self.cards.extend([Card(CardValue.JOKER, suit) for suit in joker_suits])
        self.shuffle()

    def __str__(self) -> str:
        return "\n".join(str(card) for card in self.cards)

    def __repr__(self) -> str:
        return f"CardDeck(cards={self.cards})"

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def add_card_to_top(self, card: Card) -> None:
        self.cards.append(card)

    def draw_card(self) -> Card:
        return self.cards.pop()

    def draw_cards(self, count: int ) -> list[Card]:
        return [self.draw_card() for _ in range(count)]

    def size(self) -> int:
        return len(self.cards)
