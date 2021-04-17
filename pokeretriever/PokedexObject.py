import abc
"""
This module contains the abstract and concrete classes for all objects that the Pokedex creates
"""

class PokedexObject(abc.ABC):
    """
    ABC for a pokedex object
    """
    @abc.abstractmethod
    def __init__(self, name, id, **kwargs):
        """
        Base Constructor
        :param name: Name as string
        :param id: ID as int
        :param kwargs: Dictionary containing extra information
        """
        self._name = name
        self._id = id

    @property
    def name(self):
        """
        Name of object
        :return: name
        """
        return self._name

    @property
    def poke_id(self):
        """
        ID of object
        :return: ID
        """
        return self._id


class Pokemon(PokedexObject):
    """
    Pokemon Object that is created from the PokeAPI
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
        self._expanded = False

    @property
    def height(self):
        """
        Height of the pokemon
        :return: int
        """
        return self._height

    @property
    def weight(self):
        """
        Weight of the pokemon
        :return:
        """
        return self._weight

    @property
    def stats(self):
        """
        List of stats of the pokemon
        :return: If expanded -> return list of PokeStat objects
                else -> return formatted string list of stats
        """
        stat_list = []
        if self._expanded:
            return self._stats
        else:
            for stats in self._stats:
                name = stats['stat']['name']
                base_stat = stats['base_stat']
                string_stat = f"{name}, {base_stat}"
                stat_list.append(string_stat)
            return "\n".join(stat_list)

    def stat_list(self):
        """
        Returns the Pokemons stat names in a list.
        Used as a helper method for creating PokeStat objects
        :return: a list representing the Pokemons extended stats
        """
        stat_list = []
        for stats in self._stats:
            name = stats['stat']['name']
            stat_list.append(name)
        return stat_list

    @stats.setter
    def stats(self, value):
        """
        Stats setter
        Only used when expanded is flagged as true
        :param value: List of PokeStat objects
        :return:
        """
        self._expanded = True
        self._stats = value

    @property
    def types(self):
        """
        List of types for the Pokemon
        :return: String containing the pokemon types
        """
        list_type = ''
        for types in self._types:
            type_dict = types['type']
            type_name = type_dict['name']
            list_type += type_name + ' '
        return list_type

    @property
    def abilities(self):
        """
        List of pokemon abilities
        :return: If expanded -> return list of PokeAbility objects
        else -> return string list of ability names
        """
        ability_list = []
        if self._expanded:
            return self._abilities
        else:
            for ability in self._abilities:
                name = ability['ability']['name']
                ability_list.append(name)
            return "\n".join(ability_list)

    def ability_list(self):
        """
        Gets a list of ability names
        Helper method for creating PokeAbility objects
        :return:
        """
        ability_list = []
        for ability in self._abilities:
            ability_list.append(ability['ability']['name'])
        return ability_list

    @abilities.setter
    def abilities(self, value):
        """
        Abilities setter
        Used only when expanded is true
        :param value: list of PokeAbility objects
        :return:
        """
        self._expanded = True
        self._abilities = value

    @property
    def moves(self):
        """
        List of pokemon moves
        :return: If expanded -> return list of PokeMove objects
        else -> return string list of move names and some details
        """
        move_list = []
        if self._expanded:
            return self._moves
        for move in self._moves:
            name = move['move']['name']
            level_acquired = str(move['version_group_details'][0]['level_learned_at'])
            string_move = f"Move name: {name}, Level acquired: {level_acquired}"
            move_list.append(string_move)
        return "\n".join(move_list)

    def move_list(self):
        """
        Gets a list of move names
        Helper method for creating PokeMove objects
        :return:
        """
        move_list = []
        for move in self._moves:
            move_list.append(move['move']['name'])
        return move_list

    @moves.setter
    def moves(self, value):
        """
        Moves setter
        Used only when expanded is true
        :param value: list of PokeMove objects
        :return:
        """
        self._expanded = True
        self._moves = value

    def __str__(self):
        """
        toString for Pokemon
        :return: formatted string containing details of the Pokemon
        """
        if self._expanded:
            expanded_abilities = ""
            expanded_moves = ""
            expanded_stats = ""
            for ability in self._abilities:
                expanded_abilities += str(ability)
            for move in self._moves:
                expanded_moves += str(move)
            for stat in self._stats:
                expanded_stats += str(stat)
            return f"Name: {self.name} \n" \
                   f"ID: {self.poke_id} \n" \
                   f"Height: {self.height} \n" \
                   f"Weight: {self.weight} \n" \
                   f"Types: {self.types} \n" \
                   f"\nStats:\n" \
                   f"------\n" \
                   f"{expanded_stats}\n" \
                   f"\nAbilities:\n" \
                   f"------\n" \
                   f"{expanded_abilities}\n" \
                   f"\nMoves:\n" \
                   f"------\n" \
                   f"{expanded_moves}"
        else:
            return f"Name: {self.name} \n" \
               f"ID: {self.poke_id} \n" \
               f"Height: {self.height} \n" \
               f"Weight: {self.weight} \n" \
               f"Types: {self.types} \n" \
               f"\nStats:\n" \
               f"------\n" \
               f"{self.stats}\n" \
               f"\nAbilities:\n" \
               f"------\n" \
               f"{self.abilities}\n" \
               f"\nMoves:\n" \
               f"------\n" \
               f"{self.moves}"


class PokemonAbility(PokedexObject):
    """
    Pokemon Ability
    """
    def __init__(self, generation, effect_entries, pokemon, **kwargs):
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
        self._effect = effect_entries
        self._pokemon = pokemon

    @property
    def generation(self):
        """
        Generation of the ability
        :return: string name of the generation
        """
        return self._generation['name']

    @property
    def effect(self):
        """
        Gets expanded list of the ability effects
        :return:
        """
        list_effect = []
        for effect in self._effect:
            if effect['language']['name'] == 'en':
                list_effect.append(effect['effect'])
        return "\n".join(list_effect)

    @property
    def short_effect(self):
        """
        Gets shortened list of ability effects
        :return:
        """
        list_short_effect = []
        for short_effect in self._effect:
            if short_effect['language']['name'] == 'en':
                list_short_effect.append(short_effect['short_effect'])
        return "\n".join(list_short_effect)

    @property
    def pokemon(self):
        """
        Get list of pokemon that have the ability
        :return:
        """
        list_pokemon = []
        for pokemon in self._pokemon:
            list_pokemon.append(pokemon['pokemon']['name'])
        return ", ".join(list_pokemon)

    def __str__(self):
        """
        Formatted string of the ability containing the details
        :return:
        """
        return f"Name: {self.name}\n" \
               f"ID: {self.poke_id}\n" \
               f"Generation: {self.generation}\n" \
               f"Effect: {self.effect}\n" \
               f"Effect (Short): {self.short_effect}\n" \
               f"Pokemon: {self.pokemon}\n\n"

    def __repr__(self):
        return self.__str__()


class PokemonStat(PokedexObject):
    """
    Pokemon Stat
    """
    def __init__(self, is_battle_only, move_damage_class, **kwargs):
        """
        Constructor
        :param is_battle_only:
        :param move_damage_class:
        :param kwargs:
        """
        super().__init__(**kwargs)
        self._is_battle_only = is_battle_only
        self._move_damage_class = move_damage_class

    @property
    def move_damage_class(self):
        """
        Returns a string describing the move damage class.
        :return: a string
        """
        if self._move_damage_class is None:
            self._move_damage_class = "N/A"
        else:
            self._move_damage_class = self._move_damage_class['name']
        return self._move_damage_class

    @property
    def is_battle_only(self):
        """
        Returns a boolean value if the user is requesting more details.
        :return: a boolean.
        """
        return self._is_battle_only

    def __str__(self):
        """
        Returns a string representing the Pokemons Stat.
        :return: a string.
        """
        return f"Name: {self.name}\n" \
               f"ID: {self.poke_id}\n" \
               f"Is_Battle_Only: {self.is_battle_only}\n" \
               f"Move Damage Class: {self.move_damage_class}\n\n"

    def __repr__(self):
        """
        Returns a string representing the Query.
        :return: a string.
        """
        return self.__str__()


class PokemonMove(PokedexObject):
    """
    Pokemon Move
    """
    def __init__(self, generation, accuracy, pp, power, type, damage_class, effect_entries, **kwargs):
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
        self._short_effect = effect_entries

    @property
    def generation(self):
        """
        Gets the generation name
        :return:
        """
        return self._generation['name']

    @property
    def accuracy(self):
        """
        Gets the accuracy
        :return:
        """
        return self._accuracy

    @property
    def pp(self):
        """
        Gets the PP
        :return:
        """
        return self._pp

    @property
    def power(self):
        """
        Gets the power
        :return:
        """
        return self._power

    @property
    def type(self):
        """
        Gets the move type
        :return:
        """
        return self._type['name']

    @property
    def damage_class(self):
        """
        Gets the move damage class
        :return:
        """
        return self._damage_class['name']

    @property
    def short_effect(self):
        """
        Gets the shortened description of the move effect
        :return:
        """
        list_effect = []
        for effect in self._short_effect:
            list_effect.append(effect['short_effect'])
        return "".join(list_effect)

    def __str__(self):
        """
        Gets formatted string of move details
        :return:
        """
        return f"Name: {self.name}\n" \
               f"ID: {self.poke_id}\n" \
               f"Generation: {self.generation}\n" \
               f"Accuracy: {self.accuracy}\n" \
               f"PP: {self.pp}\n" \
               f"Power: {self.power}\n" \
               f"Type: {self.type}\n" \
               f"Damage Class: {self.damage_class}\n" \
               f"Effect (Short): {self.short_effect}\n\n"
