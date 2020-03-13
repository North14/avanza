import json
from datetime import datetime

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

    @property
    def info(self):
        """Grabs full json of returned news

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
        return self.data['news']

    @property
    def pretty(self):
        """Prints the news in a prettier format

        Returns:
            str:
        """
        string = ""
        for news in self.data['news']:
            string += f"\033[1mTitle:\033[0m {news['title']}\n"
            time = datetime.strptime(news['publishDateTime'], '%Y-%m-%dT%H:%M:%S%z')
            string += f"\033[1mPublished:\033[0m {time:%d-%m-%Y %H:%M}\n"
            string += f"\033[1mUrl:\033[0m {BASE_URL}{news['url']}.html\n"
            string += f"\033[1mText:\033[0m {news['text']}\n"
            string += "\n"
        return string
