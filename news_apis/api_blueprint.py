import requests


"""
This class is a blueprint class for all the news APIs. We represent
each API as a class that inherits its proporties from this super class. 
"""
class API_Inf(object):

    def __init__(self, list_url, search_url, API_KEY=None, headers={}):
        super(API_Inf, self).__init__()
        self.headers = headers
        self.API_KEY = API_KEY
        self.list_url = list_url
        self.search_url = search_url

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

    def get_search_result(self, query, limit=10):
        search_url = self.search_url.format(api_key=self.API_KEY, query=query, limit=limit)
        search_news = requests.get(search_url, headers=self.headers).json()
        return self.parse_news(search_news)

    def get_list_result(self, limit=10):
        list_url = self.list_url.format(api_key=self.API_KEY, limit=limit)
        list_news = requests.get(list_url, headers=self.headers).json()
        return self.parse_news(list_news)