"""
To add a new API:
    - Read the fi
    - Create a class that inherits from API_Inf
    - Override the function parse_news to define how the json response returned
      by the new API will be parsed to be in the right formats
    - Add the new API to the external APIs list 'EXT_API' + the needed arguments 
"""
from api_blueprint import API_Inf


class News_API(API_Inf):
    def parse_news(self, news):
        articles = news['articles']
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


# All registred external APIs
EXT_API = [
    News_API(
        list_url = ('https://newsapi.org/v2/everything'
                    '?pageSize={limit}'
                    '&apiKey={api_key}'
        ),
        
        search_url = ('https://newsapi.org/v2/top-headlines'
                      '?category=general'
                      '&q={query}'
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