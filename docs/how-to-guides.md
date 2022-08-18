To start with tutorials, go to aggreppaer's 
[GitHub repo](https://github.com/ammarkarkour/aggrepapper) and make sure you 
follow the instructions in the README file to get aggrepapper runnig.

## How To List News?
Aggrepapper is an API that supports two functionalities. The first one is to list 
the aggregated news. To do that, assuming your server is running locally on port
`8080`:

#### `REQUEST`
```
curl  http://0.0.0.0:8080/news/
```

#### `RESPONSE`
```
[
    {
        "headline": "title of the article",
        "link": "link to the original article",
        "source": "the api that this was found in"
    },
    ...
]
```



## How To Search Search Through The News?
The second functionality that Aggrepapper supports is to search the news for
articles that contain the query string.To do that, assuming your server is 
running locally on port `8080`, and you want to search for `tennis`

#### `REQUEST`
```
curl  http://0.0.0.0:8080/news/?query=tennis
```

#### `RESPONSE`
```
[
    {
        "headline": "title of the article",
        "link": "link to the original article",
        "source": "the api that this was found in"
    },
    ...
]
```
## How To Run And Add Tests?
Aggrepapper comes with unit tests that test that it works correctly. These tests 
can be found int file `test_api.py`. We use Python's 
[unittest](https://docs.python.org/3/library/unittest.html) and FastAPI's 
[TestClient](https://fastapi.tiangolo.com/tutorial/testing/) to automate 
the testing process through simulating client requests.

#### `To run the testcases`
```
python test_api.py
```

#### `Expected result`
```
..
----------------------------------------------------------------------
Ran 2 tests in 4.668s

OK

```


#### `To add a new test case`
```
- In the TestAggrepapper class, define a new method that starts with `test_`
```


## How To Add A New External API?
One of the main goals of the code design of this project is to make adding a new
news external API easy and intuitive. This is why adding a new External news API 
is as easy as defining a one method in the file `news_apis/registered_apis.py`.
For more details on how to do that spacifically, read the file 
`news_apis/registered_apis.py`