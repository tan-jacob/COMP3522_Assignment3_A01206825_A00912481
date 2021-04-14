import argparse
import pokeretriever as poke
from pokedex import Pokedex


class Request:
    """
    The request object represents a request to either return a pokemon, pokemon move
    or pokemon ability data from the Pokedex.
    """
    def __init__(self):
        """
        mode: Can be 'pokemon', 'ability' or 'move', input can be id or name
        input_type: Can be 'filename.txt' or 'name or id'
        expanded: Optional flag. Certain attributes are expanded if true
        output: Optional flag. If true, a filename must also be provided. Result will
                be printed into the provided file. If not, result will be printed to
                console
        """
        self.mode = None
        self.input_file = None
        self.input_data = None
        self.expanded = None
        self.output = None
        self.raw_data = None
        self.result = None
        self.number_of_requests = None

    def __str__(self):
        return f"Mode: {self.mode}, Input File: {self.input_file}, Input Data: {self.input_data}" \
                f", Expanded: {self.expanded}, Output: {self.output}"


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
    parser.add_argument("mode", help="Specify the mode that the pokedex will be opened in"
                                     "This must be 'pokemon', 'ability' or 'move'")

    group_in = parser.add_mutually_exclusive_group()
    group_in.add_argument("--inputfile", help="File input, must be in .txt")
    group_in.add_argument("--inputdata", nargs='+', help="Data input, must be name or id")

    parser.add_argument("-e", "--expanded", default=False,
                        help="Optional flag. Certain attributes will be expanded if included"
                             "Default set to false")
    parser.add_argument("-o", "--output", default="print",
                        help="The way the output will be formatted"
                             "By default will print to console"
                             "Can provide a .txt file to be printed to")

    try:
        args = parser.parse_args()
        r = Request()
        r.mode = PokedexMode(args.mode)
        r.input_file = args.inputfile
        r.input_data = args.inputdata
        r.expanded = args.expanded
        r.output = args.output
        print(r)

        pokedex = Pokedex()
        pokedex.execute_request(r)
        return r
    except Exception as e:
        print(f"Error! Could not read arguments.\n{e}")
        quit()
