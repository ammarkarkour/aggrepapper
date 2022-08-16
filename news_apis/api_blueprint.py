import requests


"""
This class is a blueprint class for all the news APIs. We represent
each API as a class that inherits its proporties from this super class. 
"""
class API_Inf(object):

    def __init__(self, list_url, search_url, API_KEY=None, headers={}):
        """
        - search_url must contain positional argument 'query'
        - If API key is needed, both list_url and search_url must contain
          positional argument 'api_key'
        """
        super(News_API, self).__init__()
        self.headers = headers
        self.list_url = list_url.format(api_key=API_KEY)
        self.search_url = search_url.format(api_key=API_KEY)

    def parse_news(self, news):
        """
        - REQUIRES: news: JSON
        - ENSURES: result = parse_news(news), 
          where result is a list of dictionaries of the following form:
          {
              "headline": article["title"],
              "link": article["url"],
              "source":"newsapi"
          }
        """
        pass

    def get_search_result(self, query, limit=''):
        """
        - query must be passed as positional argument
        - limit is optional argumnet that could be passed as positional argument
        """
        search_url = self.search_url.format(query=query, limit=limit)
        search_news = requests.get(search_url, headers=self.headers).json()
        return parse_news(search_news)

    def get_list_result(self, limit=''):
        """
        - limit is optional argumnet that could be passed as positional argument
        """
        list_url = self.list_url.format(limit=10)
        list_news = requests.get(self.list_url, headers=self.headers).json()
        return parse_news(list_news)