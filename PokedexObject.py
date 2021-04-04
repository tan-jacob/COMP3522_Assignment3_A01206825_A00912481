import abc


class PokedexObject(abc.ABC):
    """
    ABC for a pokedex object
    """
    @abc.abstractmethod
    def __init__(self, name, poke_id, **kwargs):
        """
        Base Constructor
        :param name: Name as string
        :param id: ID as int
        :param kwargs: Dictionary containing extra information
        """
        self._name = name
        self._poke_id = poke_id

    @property
    def name(self):
        return self._name

    @property
    def poke_id(self):
        return self._poke_id


class Pokemon(PokedexObject):
    """
    Pokemon Object
    """
    def __init__(self, height, weight, stats, types, abilities, moves, **kwargs):
        """
        Constructor
        :param height: int
        :param weight: int
        :param stats: PokemonStat list
        :param types: String list
        :param abilities: PokemonAbility list
        :param moves: PokemonMove list
        :param kwargs: name and poke_id
        """
        super().__init__(**kwargs)
        self._height = height
        self._weight = weight
        self._stats = stats
        self._types = types
        self._abilities = abilities
        self._moves = moves

    @property
    def height(self):
        return self._height

    @property
    def weight(self):
        return self._weight

    @property
    def stats(self):
        return self._stats

    @property
    def types(self):
        return self._types

    @property
    def abilities(self):
        return self._abilities

    @property
    def moves(self):
        return self._moves


class PokemonAbility(PokedexObject):
    """
    Pokemon Ability
    """
    def __init__(self, generation, effect, short_effect, pokemon, **kwargs):
        """
        Constructor
        :param generation: String
        :param effect: String
        :param short_effect: String
        :param pokemon: List of pokemon names
        :param kwargs: name and poke_id
        """
        super().__init__(**kwargs)
        self._generation = generation
        self._effect = effect
        self._short_effect = short_effect
        self._pokemon = pokemon

    @property
    def generation(self):
        return self._generation

    @property
    def effect(self):
        return self._effect

    @property
    def short_effect(self):
        return self._short_effect

    @property
    def pokemon(self):
        return self._pokemon


class PokemonStat(PokedexObject):
    """
    Pokemon Stat
    """
    def __init__(self, isBattleOnly, **kwargs):
        """
        Constructor
        :param isBattleOnly: bool
        :param kwargs: name and poke_id
        """
        super().__init__(**kwargs)
        self._isBattleOnly = isBattleOnly

    @property
    def isBattleOnly(self):
        return self._isBattleOnly


class PokemonMove(PokedexObject):
    """
    Pokemon Move
    """
    def __init__(self, generation, accuracy, pp, power, type, damage_class, short_effect, **kwargs):
        """
        Constructor
        :param generation: String
        :param accuracy: Int
        :param pp: Int
        :param power: Int
        :param type: String
        :param damage_class: String
        :param short_effect: String
        :param kwargs: Name and poke_id
        """
        super().__init__(**kwargs)
        self._generation = generation
        self._accuracy = accuracy
        self._pp = pp
        self._power = power
        self._type = type
        self._damage_class = damage_class
        self._short_effect = short_effect

    @property
    def generation(self):
        return self._generation

    @property
    def accuracy(self):
        return self._accuracy

    @property
    def pp(self):
        return self._pp

    @property
    def power(self):
        return self._power

    @property
    def type(self):
        return self._type

    @property
    def damage_class(self):
        return self._damage_class

    @property
    def short_effect(self):
        return self._short_effect

