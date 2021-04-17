import argparse
import pokeretriever.RequestHandlers as Handlers
import pokeretriever.Enums as Enums
import pokeretriever.Request as Request


class Pokedex:
    """
    Facade class that interacts with the pokeretriever package to execute requests
    """

    def __init__(self):
        """
        Base Constructor
        """
        input_handler = Handlers.InputHandler()
        self.start_handler = input_handler

    def execute_request(self, r: Request):
        """
        Executes the given request. Builds the handler chain depending on the selected mode
        :param r: request
        :return:
        """
        pokemon_handler = Handlers.PokemonRequestHandler()
        move_handler = Handlers.MoveRequestHandler()
        ability_handler = Handlers.AbilityRequestHandler()
        expanded_handler = Handlers.PokemonExpandedHandler()
        output_handler = Handlers.OutputHandler()

        if r.mode == Enums.PokedexMode.POKEMON:
            if r.expanded:
                expanded_handler.set_handler(output_handler)
                self.start_handler.set_handler(expanded_handler)
            else:
                pokemon_handler.set_handler(output_handler)
                self.start_handler.set_handler(pokemon_handler)
        elif r.mode == Enums.PokedexMode.ABILITY:
            ability_handler.set_handler(output_handler)
            self.start_handler.set_handler(ability_handler)
        elif r.mode == Enums.PokedexMode.MOVE:
            move_handler.set_handler(output_handler)
            self.start_handler.set_handler(move_handler)

        self.start_handler.handle_request(r)


def setup_request_commandline() -> Request:
    """
    Implements the argparse module to accept arguments via the command
    line. This function specifies what these arguments are and parses it
    into an object of type Request. If something goes wrong with
    provided arguments then the function prints an error message and
    exits the application.
    :return: The object of type Request with all the arguments provided
    in it.
    """
    parser = argparse.ArgumentParser()

    group_in = parser.add_mutually_exclusive_group()
    group_in.add_argument("--inputfile", help="File input, must be in .txt")
    group_in.add_argument("--inputdata", help="Data input, must be name or id")

    parser.add_argument("-e", "--expanded", default=False, action='store_true',
                        help="Optional flag. Certain attributes will be expanded if included"
                             "Default set to false")
    parser.add_argument("-o", "--output", default="print",
                        help="The way the output will be formatted"
                             "By default will print to console"
                             "Can provide a .txt file to be printed to")

    parser.add_argument("mode", help="Specify the mode that the pokedex will be opened in"
                                     "This must be 'pokemon', 'ability' or 'move'")

#try:
    args = parser.parse_args()
    r = Request.Request()
    r.mode = Enums.PokedexMode(args.mode)
    r.input_file = args.inputfile
    r.input_data = args.inputdata
    r.expanded = args.expanded
    r.output = args.output
    print(r)

    pokedex = Pokedex()
    pokedex.execute_request(r)
    return r
# except Exception as e:
#     print(f"Error! Could not read arguments.\n{type(e)}")



def main(r: Request):
    pass


if __name__ == '__main__':
    request = setup_request_commandline()
    main(request)
