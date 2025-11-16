# game/cards/card.py

from .enums import Color, Value, VALUE_MAP, Suit, SUIT_COLORS, JOKER_COLORS

class Card:
    color: Color
    value: Value
    rank: int
    suit: Suit | None

    def __init__(self, value: Value, suit: Suit | None = None, color: Color | None = None) -> None:
        if color is None:
            if suit is None:
                raise ValueError("Must provide either suit or color")
            self.color = SUIT_COLORS[suit]
        else:
            if color not in JOKER_COLORS:
                raise ValueError(f"Invalid color: {color}")
            self.color = color
        self.value = value
        self.rank = VALUE_MAP[value]
        self.suit = suit

    def __str__(self) -> str:
        return f"{self.color} {self.value} ({self.rank}) {self.suit}"

    def __repr__(self) -> str:
        return f"Card(color={self.color}, value={self.value}, rank={self.rank}, suit={self.suit})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Card):
            return False
        return self.color == other.color and self.value == other.value
