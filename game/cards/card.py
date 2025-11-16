# game/cards/card.py

from .enums import Color, Value, VALUE_MAP, Suit, SUIT_COLORS, SUIT_SYMBOLS

class Card:
    color: Color
    value: Value
    rank: int
    suit: Suit
    symbol: str

    def __init__(self, value: Value, suit: Suit, color: Color | None = None) -> None:
        if color is None:
            suit_color = SUIT_COLORS[suit]
            if isinstance(suit_color, tuple):
                raise ValueError(f"Color must be explicitly provided for suit {suit}")
            self.color = suit_color
        else:
            self.color = color
        self.value = value
        self.rank = VALUE_MAP[value]
        self.suit = suit
        self.symbol = SUIT_SYMBOLS[suit]

    def __str__(self) -> str:
        return f"{self.color} {self.value} ({self.rank}) {self.symbol}"

    def __repr__(self) -> str:
        return f"Card(color={self.color}, value={self.value}, rank={self.rank}, suit={self.suit}, symbol={self.symbol})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Card):
            return False
        return self.color == other.color and self.value == other.value
