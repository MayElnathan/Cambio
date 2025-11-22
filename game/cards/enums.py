from enum import Enum, IntEnum

class Color(Enum):
    RED = "red"
    BLACK = "black"

class CardValue(IntEnum):
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

CARD_VALUE_TO_POINTS: dict[CardValue, int] = {
    CardValue.JOKER: 0,
    CardValue.ACE: 1,
    CardValue.TWO: 2,
    CardValue.THREE: 3,
    CardValue.FOUR: 4,
    CardValue.FIVE: 5,
    CardValue.SIX: 6,
    CardValue.SEVEN: 7,
    CardValue.EIGHT: 8,
    CardValue.NINE: 9,
    CardValue.TEN: 10,
    CardValue.JACK: 10,
    CardValue.QUEEN: 10,
    CardValue.KING: 10,
}

class Action(Enum):
    PEEK_AT_SELF_CARD = "peek_at_self_card"
    PEEK_AT_OTHER_CARD = "peek_at_other_card"
    BURN_OTHER_CARD = "burn_other_card"
    SWAP_TWO_CARDS = "swap_two_cards"
    TWO_PEEKS_ONW_SWAP_CARDS = "two_peeks_onw_swap_cards"

CARD_VALUE_TO_ACTION: dict[CardValue, Action] = {
    CardValue.SEVEN: Action.PEEK_AT_SELF_CARD,
    CardValue.EIGHT: Action.PEEK_AT_SELF_CARD,
    CardValue.NINE: Action.PEEK_AT_OTHER_CARD,
    CardValue.TEN: Action.PEEK_AT_OTHER_CARD,
    CardValue.JACK: Action.BURN_OTHER_CARD,
    CardValue.QUEEN: Action.SWAP_TWO_CARDS,
    CardValue.KING: Action.TWO_PEEKS_ONW_SWAP_CARDS,
}

class Suit(Enum):
    HEARTS = "Hearts"
    DIAMONDS = "Diamonds"
    CLUBS = "Clubs"
    SPADES = "Spades"
    RED_JOKER = "Red Joker"
    BLACK_JOKER = "Black Joker"

CARD_SUIT_TO_SYMBOLS: dict[Suit, str] = {
    Suit.HEARTS: "♥",
    Suit.DIAMONDS: "♦",
    Suit.CLUBS: "♣",
    Suit.SPADES: "♠",
    Suit.RED_JOKER: "Red Joker",
    Suit.BLACK_JOKER: "Black Joker",
}



CARD_SUIT_COLORS: dict[Suit, Color] = {
    Suit.HEARTS: Color.RED,
    Suit.DIAMONDS: Color.RED,
    Suit.CLUBS: Color.BLACK,
    Suit.SPADES: Color.BLACK,
    Suit.RED_JOKER: Color.RED,
    Suit.BLACK_JOKER: Color.BLACK,
}


