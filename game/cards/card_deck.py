# game/cards/card_deck.py

import random

from .card import Card
from .enums import Suit, Value, JOKER_COLORS

class CardDeck:
    cards: list[Card]

    def __init__(self) -> None:
        self.cards = [Card(value, suit) for suit in Suit for value in Value if value != Value.JOKER]
        self.cards.extend([Card(Value.JOKER, None, color) for color in JOKER_COLORS])
        self.shuffle()

    def __str__(self) -> str:
        return "\n".join(str(card) for card in self.cards)

    def __repr__(self) -> str:
        return f"CardDeck(cards={self.cards})"

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def draw(self) -> Card:
        return self.cards.pop()

    def draw_cards(self, count: int = 1) -> list[Card]:
        return [self.cards.pop() for _ in range(count)]