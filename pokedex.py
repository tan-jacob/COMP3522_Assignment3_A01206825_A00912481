from pokeretriever import *

import Request


class Pokedex:
    """

    """
    def __init__(self):
        """
        Base Constructor
        """
        input_handler = InputHandler()
        self.start_handler = input_handler

    def execute_request(self, r: Request):
        """
        Executes the given request. Builds the handler chain depending on the selected mode
        :param r: request
        :return:
        """
        pokemon_handler = PokemonRequestHandler()
        move_handler = MoveRequestHandler()
        ability_handler = AbilityRequestHandler()
        expanded_handler = PokemonExpandedHandler()
        output_handler = OutputHandler()

        if r.mode == PokedexMode.POKEMON:
            if r.expanded == "True":
                expanded_handler.set_handler(output_handler)
                self.start_handler.set_handler(expanded_handler)
            else:
                pokemon_handler.set_handler(output_handler)
                self.start_handler.set_handler(pokemon_handler)
        elif r.mode == PokedexMode.ABILITY:
            ability_handler.set_handler(output_handler)
            self.start_handler.set_handler(ability_handler)
        elif r.mode == PokedexMode.MOVE:
            move_handler.set_handler(output_handler)
            self.start_handler.set_handler(move_handler)

        self.start_handler.handle_request(r)


def main(r: Request):
    pass


if __name__ == '__main__':
    request = Request.setup_request_commandline()
    main(request)
