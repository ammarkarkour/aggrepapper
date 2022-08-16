from typing import Union
from fastapi import FastAPI
from news_apis.registered_apis import EXT_API

app = FastAPI()

@app.get("/news/")
def get_news(query: Union[str, None] = None):
    result = []
    if query: # Search
        for api in EXT_API:
            result.append(api.get_search_result(query))
    else:
        for api in EXT_API:
            result.append(api.get_list_result(query))

    return result