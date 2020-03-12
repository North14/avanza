import json

from .constants import constants, BASE_URL
from .base import Base


class Search(Base):
    def __init__(self, search_query):
        """Returns results of search query

        Args:
            searchQuery (str): The string to be searched at Avanza
        """
        super().__init__()
        url = f"{BASE_URL}{constants['paths']['SEARCH']}".format(search_query)
        self.data = self._request(url)

    def __str__(self):
        return json.dumps(self.data)

    def info(self):
        return self.data
