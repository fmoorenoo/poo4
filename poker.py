from __future__ import annotations


def load_card_glyphs(path: str = 'cards.dat') -> dict[str, str]:
    diccionario = {"♣": "🃑🃒🃓🃔🃕🃖🃗🃘🃙🃚🃛🃝🃞", "◆": "🃁🃂🃃🃄🃅🃆🃇🃈🃉🃊🃋🃍🃎", "❤": "🂱🂲🂳🂴🂵🂶🂷🂸🂹🂺🂻🂽🂾", "♠": "🂡🂢🂣🂤🂥🂦🂧🂨🂩🂪🂫🂭🂮"}
    return diccionario


class Card:
    CLUBS = "♣"
    DIAMONDS = "◆"
    HEARTS = "❤"
    SPADES = "♠"
    #           1,   2,   3,   4,   5,   6,   7,   8,   9,   10,  11,  12,  13
    SYMBOLS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
    A_VALUE = 1
    K_VALUE = 13
    GLYPHS = load_card_glyphs()

    def __init__(self, value: int | str, suit: str):
        if suit not in [self.CLUBS, self.DIAMONDS, self.HEARTS, self.SPADES]:
            raise InvalidCardError(f"🃏 Invalid card: {repr(suit)} is not a supported suit")
        
        if isinstance(value, int):
            if value < 1 or value > 13:
                raise InvalidCardError(f"🃏 Invalid card: {repr(value)} is not a supported value")
            self.value = value
        
        elif isinstance(value, str):
            if value not in Card.SYMBOLS:
                raise InvalidCardError(f"🃏 Invalid card: {repr(value)} is not a supported symbol")
            self.value = value
        self.suit = suit

    @property
    def cmp_value(self) -> int:
        '''Devuelve el valor (numérico) de la carta para comparar con otras.
        Tener en cuenta el AS.'''
        if isinstance(self.value, int):
            return self.value
        elif self.value == 'A': 
            return 1
        elif self.value == 'J': 
            return 11
        elif self.value == 'Q': 
            return 12
        elif self.value == 'K': 
            return 13

    def __repr__(self):
        '''Devuelve el glifo de la carta'''
        return self.GLYPHS[self.suit][self.cmp_value - 1]


    def __eq__(self, other: Card | object):
        if self.suit == other.suit:
            if self.value == other.value:
                return True
        return False

    def __lt__(self, other: Card):
        '''Indica si una carta vale menos que otra'''
        if self.cmp_value > other.cmp_value:
            return True
        return False

    def __gt__(self, other: Card):
        '''Indica si una carta vale más que otra'''
        if self.cmp_value < other.cmp_value:
            return True
        return False


    def __add__(self, other: 'Card') -> 'Card':
        if self.value == 1:
            total = 1
            nuevoSuit = self.suit
        else:
            total = self.value + other.value
            if self.value >= other.value:
                nuevoSuit = self.suit
            else:
                nuevoSuit = other.suit
    
        if total > 13:
            total = 1

        return Card(total, nuevoSuit)
    

    def is_ace(self) -> bool:
        return self.value == 'A'


    @classmethod
    def get_available_suits(cls) -> str:
        return cls.CLUBS + cls.DIAMONDS + cls.HEARTS + cls.SPADES


    @classmethod
    def get_cards_by_suit(cls, suit: str):
        lista = []
        for glifo in cls.GLYPHS[suit]:
            lista.append(glifo)
        return lista


class InvalidCardError(Exception):
    def __init__(self, message="🃏 Invalid card"):
        self.message = message

    def __str__(self):
        return self.message

