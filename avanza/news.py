import json

from .constants import constants, BASE_URL
from .base import Base


class News(Base):
    def __init__(self, index):
        """Returns Avanza news

        Args:
            index (int): The amount of news to be returned
        """
        super().__init__()
        url = f"{BASE_URL}{constants['paths']['NEWS']}".format(index)
        self.data = self._request(url)

    def __str__(self):
        return json.dumps(self.data)

    def info(self):
        """Grabs full json of returned news

        Returns:
            dict:
        """
        return self.data
