from .enums import Color, CardValue, CARD_VALUE_TO_POINTS, Suit, CARD_SUIT_COLORS, CARD_SUIT_TO_SYMBOLS

class Card:
    _color: Color
    _value: CardValue
    _suit: Suit

    def __init__(self, value: CardValue, suit: Suit) -> None:
        self._value = value
        self._suit = suit

    def __str__(self) -> str:
        return f"{self._color} {CARD_SUIT_TO_SYMBOLS[self._suit]} {self._value} ( gives you {CARD_VALUE_TO_POINTS[self._value]} points)"

    def __repr__(self) -> str:
        return f"Card(color={self._color}, value={self._value}, points for card={CARD_VALUE_TO_POINTS[self._value]}, suit={self._suit}, symbol={CARD_SUIT_TO_SYMBOLS[self._suit]})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Card):
            return False
        return self._color == other._color and self._value == other._value
    
    def get_color(self) -> Color:
        return CARD_SUIT_COLORS[self._suit]
    
    def get_value(self) -> CardValue:
        return self._value
    
    def get_suit(self) -> Suit:
        return self._suit

    def get_points(self) -> int:
        return CARD_VALUE_TO_POINTS[self._value]

    def get_symbol(self) -> str:
        return CARD_SUIT_TO_SYMBOLS[self._suit]
