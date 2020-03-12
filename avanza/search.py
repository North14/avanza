from .constants import constants, BASE_URL
from .base import Base


class Search(Base):
    def __init__(self, search_query):
        self.search_query = search_query

    def search(self, searchQuery):
        """Returns results of search query

        Args:
            searchQuery (str): The string to be searched at Avanza

        Returns:
            dict:
        """
        url = f"{BASE_URL}{constants['paths']['SEARCH']}".format(searchQuery)
        return self._request(url)
