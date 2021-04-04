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
        self.input_type = None
        self.expanded = None
        self.output = None
