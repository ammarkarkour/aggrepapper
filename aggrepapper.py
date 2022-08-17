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
def get_news(query: Union[str, None] = None):
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