import enum


class PokedexMode(enum.Enum):
    """
    Enum for the different modes that the Pokedex supports
    """
    POKEMON = "pokemon"
    ABILITY = "ability"
    MOVE = "move"
