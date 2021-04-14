import datetime
import aiohttp
import asyncio
import Request
from pokeretriever.PokedexObject import *


async def get_pokedex_data(key, url, session) -> dict:
    """

    :param key:
    :param url:
    :param session:
    :return:
    """

    target_url = url.format(key)
    response = await session.request(method="GET", url=target_url)
    json_dict = await response.json()
    return json_dict


class BaseHandler(abc.ABC):
    """
    Base handler for the three types of requests
    """

    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    @abc.abstractmethod
    def handle_request(self, r: Request):
        pass

    def set_handler(self, handler):
        self.next_handler = handler


class InputHandler(BaseHandler):
    """
    Handle input mode for files or raw data
    """

    def handle_request(self, r: Request):
        print("Start input handler")
        if r.input_data is None:
            with open(r.input_file, mode='r') as f:
                r.raw_data = f.read().splitlines()
        else:
            r.raw_data = r.input_data
        r.number_of_requests = len(r.raw_data)
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.next_handler.handle_request(r))


class PokemonRequestHandler(BaseHandler):
    """
    Handles pokemon requests
    """

    async def handle_request(self, r: Request):
        """

        :param r:
        :return:
        """
        print("Start pokemon handler")
        url = "https://pokeapi.co/api/v2/pokemon/{}/"
        # print(r.raw_data)
        async with aiohttp.ClientSession() as session:
            async_coroutines = [get_pokedex_data(key, url, session)
                                for key in r.raw_data]
            responses = await asyncio.gather(*async_coroutines)
            poke_list = []
            for res in responses:
                poke_list.append(Pokemon(**res))
            r.result = poke_list

        self.next_handler.handle_request(r)


class PokemonExpandedHandler(BaseHandler):

    async def handle_request(self, r: Request):
        """
        Gets information from the Pokemon API.
        :param r: a request.
        :return: None.
        """
        # Get each pokemon
        url = "https://pokeapi.co/api/v2/pokemon/{}/"
        async with aiohttp.ClientSession() as session:
            async_coroutines = [get_pokedex_data(key, url, session)
                                for key in r.raw_data]

            responses = await asyncio.gather(*async_coroutines)

            list_pokemon = []

            for pokemon in responses:
                list_pokemon.append(Pokemon(**pokemon))

        for pokemon in list_pokemon:
            # Get each ability from a pokemon
            url = "https://pokeapi.co/api/v2/ability/{}/"
            async with aiohttp.ClientSession() as session:
                async_coroutines2 = [get_pokedex_data(key, url, session)
                                     for key in pokemon.ability_list()]

                responses2 = await asyncio.gather(*async_coroutines2)
                ability_list = []
                for ability in responses2:
                    ability_list.append(PokemonAbility(**ability))
                pokemon.abilities = ability_list
            # Get each move from a pokemon
            url = "https://pokeapi.co/api/v2/move/{}/"
            async with aiohttp.ClientSession() as session:
                async_coroutines3 = [get_pokedex_data(key, url, session)
                                     for key in pokemon.move_list()]

                responses3 = await asyncio.gather(*async_coroutines3)
                move_list = []
                for move in responses3:
                    move_list.append(PokemonMove(**move))
                pokemon.moves = move_list
            # Get each stat from a pokemon
            url = "https://pokeapi.co/api/v2/stat/{}/"
            async with aiohttp.ClientSession() as session:
                async_coroutines4 = [get_pokedex_data(key, url, session)
                                     for key in pokemon.stat_list()]

                responses4 = await asyncio.gather(*async_coroutines4)
                stat_list = []
                for stat in responses4:
                    stat_list.append(PokemonStat(**stat))
                pokemon.stats = stat_list

        r.result = list_pokemon

        self.next_handler.handle_request(r)


class AbilityRequestHandler(BaseHandler):
    """
    Handle ability requests
    """

    async def handle_request(self, r: Request):
        """

        :param r:
        :return:
        """
        url = "https://pokeapi.co/api/v2/ability/{}/"
        async with aiohttp.ClientSession() as session:
            async_coroutines = [get_pokedex_data(key, url, session)
                                for key in r.raw_data]
            responses = await asyncio.gather(*async_coroutines)
            ability_list = []
            for res in responses:
                ability_list.append(PokemonAbility(**res))
            r.result = ability_list

        self.next_handler.handle_request(r)


class MoveRequestHandler(BaseHandler):
    """
    Handle move requests
    """

    async def handle_request(self, r: Request):
        """

        :param r:
        :return:
        """
        url = "https://pokeapi.co/api/v2/move/{}/"
        async with aiohttp.ClientSession() as session:
            async_coroutines = [get_pokedex_data(key, url, session)
                                for key in r.raw_data]

            responses = await asyncio.gather(*async_coroutines)
            move_list = []
            for res in responses:
                move_list.append(PokemonMove(**res))
            r.result = move_list

        self.next_handler.handle_request(r)


class OutputHandler(BaseHandler):
    """

    """

    def handle_request(self, r: Request):
        if r.output == 'print':
            for response in r.result:
                print(response, "\n")
        else:
            with open(r.output, mode='w') as my_text_file:
                date = datetime.datetime.now()
                string_date = date.strftime("%d/%m/%Y %H:%M")
                my_text_file.write(f"Timestamp: {string_date}\n"
                                   f"Number of requests: {r.number_of_requests}\n")
                for response in r.result:
                    my_text_file.write(f"{response}\n")
