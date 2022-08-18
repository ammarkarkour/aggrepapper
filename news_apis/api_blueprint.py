from __future__ import annotations
import requests
from configure import config


class API_Inf(object):
    """API interface that contains the needed fields and methods for any API.
    
    Attributes
    ----------
    list_url (str): The used link to get a list of news.
    
    search_url (int): The used link to search through the news.
    
    API_KEY (str): API key if the used api needs to be called with a key (default None).
    
    headers (dict): headers that could be passed along side the get request (default {}).
    
    Methods
    -------
    parse_news(news): Parses API response and return it in the right formats

    get_search_result(query, limit=10): Use search_url to get news about a query string

    get_list_result(limit=10): Use list_url to list the top current news
    """


    def __init__(self, list_url:str, search_url:str, API_KEY:str =None, headers:dict ={}):
        super(API_Inf, self).__init__()
        self.headers = headers
        self.API_KEY = API_KEY
        self.list_url = list_url
        self.search_url = search_url


    def parse_news(self, news:list[dict[str, str]]):
        """Parse API response and return it in the right formats.

        Args:
            news: The returned API json response.

        Returns:
            List of dictionaries where ach dictionary is a news articleof the form
                {
                    "headline": "title of the article",
                    "link": "link to the original article",
                    "source": "the api that this was found in"
                }
        """
        pass


    def get_search_result(self, query:str, limit:int =config['limit']) -> list[dict[str, str]]:
        """Use search_url to get news about a query string.
        
        Args:
            query : The spacific string to be searching for.
            limit : The maximum number of news articles to be returned. 

        Returns:
            List of dictionaries where each dictionary is a news article.
        """
        search_url = self.search_url.format(api_key=self.API_KEY, query=query, limit=limit)
        search_news = requests.get(search_url, headers=self.headers).json()
        return self.parse_news(search_news)


    def get_list_result(self, limit:int =config['limit']) -> list[dict[str, str]]:
        """Use list_url to list the top current news

        Args:
            limit: The maximum number of news articles to be returned. 

        Returns:
            List of dictionaries where each dictionary is a news article.
        """
        list_url = self.list_url.format(api_key=self.API_KEY, limit=limit)
        list_news = requests.get(list_url, headers=self.headers).json()
        return self.parse_news(list_news)