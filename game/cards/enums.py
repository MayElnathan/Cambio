from enum import Enum, IntEnum

class Color(Enum):
    RED = "red"
    BLACK = "black"

class Value(IntEnum):
    JOKER = 0
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13

VALUE_MAP: dict[Value, int] = {
    Value.JOKER: 0,
    Value.ACE: 1,
    Value.TWO: 2,
    Value.THREE: 3,
    Value.FOUR: 4,
    Value.FIVE: 5,
    Value.SIX: 6,
    Value.SEVEN: 7,
    Value.EIGHT: 8,
    Value.NINE: 9,
    Value.TEN: 10,
    Value.JACK: 10,
    Value.QUEEN: 10,
    Value.KING: 10,
}

class Suit(Enum):
    HEARTS = "Hearts"
    DIAMONDS = "Diamonds"
    CLUBS = "Clubs"
    SPADES = "Spades"

SUIT_SYMBOLS: dict[Suit, str] = {
    Suit.HEARTS: "♥",
    Suit.DIAMONDS: "♦",
    Suit.CLUBS: "♣",
    Suit.SPADES: "♠",
}


JOKER_COLORS: list[Color] = [Color.BLACK, Color.RED]

SUIT_COLORS: dict[Suit, Color] = {
    Suit.HEARTS: Color.RED,
    Suit.DIAMONDS: Color.RED,
    Suit.CLUBS: Color.BLACK,
    Suit.SPADES: Color.BLACK,
}


