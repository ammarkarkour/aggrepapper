"""Register a new external API for news aggregation.

One of the main goals of the code design of this project is to make adding a new
news external API easy and intuitive. This module is used to register the API
that will be used to aggregate the news.

To add a new API:
    * Read the file news_apis/api_blueprint.py to understand the API interface
    * Create a class that inherits from API_Inf
    * Override the function parse_news to define how to parse the json-response 
        of the new API into the right format.
    * You can add new methods to the class for extra functionalities if you want
    * Define the new API and add it to the external APIs list 'API_LIST'

Guidline for defining External APIs:
    * If API key is needed:
        * 'list_url' and 'search_url' must contain positional argument 'api_key'
        * API_KEY: must be passed                           --- REQUIRED
    * list_url:
        * limit: Max number of displayed news, default = 10 --- OPTIONAL
    * search_url:
        * query: Query input to be looked for               --- REQUIRED
        * limit: Max number of displayed news, default = 10 --- OPTIONAL
    * headers could be passed if needed
"""

from .api_blueprint import API_Inf


class News_API(API_Inf):
    """Class API for newsapi API"""

    def parse_news(self, news):
        articles = news["articles"]
        result = []
        for article in articles:
            result.append({
                "headline": article["title"],
                "link": article["url"],
                "source":"newsapi"
            })
        return result

class Reddit_API(API_Inf): 
    """Class API for reddit API"""
    
    def parse_news(self, news):
        articles = news["data"]["children"]
        result = []
        for article in articles:
            result.append({
                "headline": article["data"]["title"],
                "link": article["data"]["url"],
                "source": "reddit"
            })
        return result


API_LIST = [
    News_API(
        list_url = ('https://newsapi.org/v2/everything'
                    '?pageSize={limit}'
                    '&domains=yahoo.com, naver.com, qq.com,'
                             'msn.com, bbc.co.uk, cnn.com'
                    '&apiKey={api_key}'
        ),
        search_url = ('https://newsapi.org/v2/everything'
                      '?q={query}'
                      '&pageSize={limit}'
                      '&apiKey={api_key}'
        ),
        API_KEY = 'ADD YOUR NewsAPI KEY HERE'
    ),

    Reddit_API(
        list_url = ('https://www.reddit.com/r/news/top.json'
                    '?limit={limit}'
        ),
        search_url = ('https://www.reddit.com/r/news/top.json'
                      '?q={query}'
                      '&limit={limit}'
        ),
        headers= {'User-agent': 'aggrepapper bot 0.1'}
    )
]