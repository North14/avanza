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

    @property
    def info(self):
        """Grabs full json of ticker call

        Returns:
            dict:
        """
        return self.data

    @property
    def results(self):
        """Grabs the list of results

        Returns:
            list:
        """
        return self.data['resultGroups']

    @property
    def first(self):
        """Grabs the first result

        Returns:
            Dict:

        Note:
            Results are ordered by instrument, which means stock is the most likely result
        """
        return self.data['resultGroups'][0]

    @property
    def count(self):
        """Grabs total number of hits

        Returns:
            int:
        """
        return self.data['totalNumberOfHits']

    @property
    def by_instrument(self, instrument):
        """Grabs the results filtered by instrument type

        Args:
            instrument (str): instrument type

        Returns:
            list:
        """
        instrument = instrument.upper()
        list1 = []
        if instrument in constants['public']['instruments']:
            for results in self.data['resultGroups']:
                if instrument == results['instrumentType']:
                    [list1.append(hit) for hit in results['hits']]
            return list1
        else:
            raise Exception("Invalid instrument")
