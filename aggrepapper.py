"""Aggregate news from all registered APIs.

This module defined the news aggregater API, which has 2 functionalities.
The first functionality is list, which lists the news from all the different 
registered APIs. The second functionality is search, which searches the news for
articles that contain the query string. Moreover, our implementation is inhanced
with Redis as a chaching system that works by temporarily storing information in
a key-value data structure, which we set it to expire after 1 hour in case new 
news articles got published.

This module contains the following function:

- `get_new(query)` - Returns the aggregated news.
"""

from __future__ import annotations
import json
import redis
import uvicorn
from typing import Union
from fastapi import FastAPI
from configure import config
from news_apis.registered_apis import API_LIST


app = FastAPI()
cache = redis.StrictRedis(decode_responses=True)

@app.get("/news/")
def get_news(query: Union[str, None] = None) -> list[dict[str, str]]:
    """Aggregates news from different APIs.
    
    Args:
        query: Searching for a spacific string.

    Returns:
        list of dictionaries where each dictionary is a news article
    """
    news = []

    # Search
    if query:

        # News in cache
        found_cached_news = cache.get(query)    
        if found_cached_news:  
            news = json.loads(found_cached_news)
    
            return news

        # News not in cache
        for api in API_LIST:
            news += api.get_search_result(query)
        cache.set(query, json.dumps(news), config['redis-exp-time'])

        return news

    # List
    found_cached_news = cache.get("agrepapper-search")
    if found_cached_news:
        news = json.loads(found_cached_news)
        
        return news
    
    for api in API_LIST:
        news += api.get_list_result()
    cache.set("agrepapper-search", json.dumps(news), config['redis-exp-time'])
    
    return news


if __name__ == "__main__":
    uvicorn.run(app, host=config['host'], port=config['port'])