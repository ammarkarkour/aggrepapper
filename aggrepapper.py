import uvicorn
from typing import Union
from fastapi import FastAPI
from news_apis.registered_apis import EXT_API

app = FastAPI()

@app.get("/news/")
def get_news(query: Union[str, None] = None):
    result = []
    if query: # Search
        for api in EXT_API:
            result += api.get_search_result(query)
    else: # List
        for api in EXT_API:
            result += api.get_list_result()

    return result


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)