"""
To add a new API:
    - Read the file news_apis.api_blueprint.py to understand the API interface
    - Create a class that inherits from API_Inf
    - Override the function parse_news to define how to parse the json-response
        of the new API into the right format.
    - You can add new methods to the class for extra functionalities if you want
    - Add the new API to the external APIs list 'EXT_API'
"""
from .api_blueprint import API_Inf


class News_API(API_Inf):
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


"""
Guidline for defining External APIs:

- list_url:
    - 'limit' is optional argumnet that could be passed as positional argument

- search_url:
    - Must contain positional argument 'query'
    - 'limit' is optional argumnet that could be passed as positional argument

- If API key is needed:
    - list_url and search_url must contain positional argument 'api_key'
    - API_KEY must be passed

- headers could be passed if needed
"""

EXT_API = [
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
        API_KEY = '8d8548be01a44759a18214854ed27de2'
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