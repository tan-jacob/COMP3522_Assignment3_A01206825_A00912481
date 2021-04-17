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
        self.result = []
        self.number_of_requests = None

    def __str__(self):
        return f"Mode: {self.mode}, Input File: {self.input_file}, Input Data: {self.input_data}" \
               f", Expanded: {self.expanded}, Output: {self.output}"
