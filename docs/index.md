This site contains the project documentation for the `Aggrepapper` project that 
is a news aggregator from different APIs. Its aim is to aggregate  news from 
different APIs and display them to users, while making it easy for developers 
to add new external news APIs to aggregate news from them.

To build our API we use [FastAPI](https://github.com/tiangolo/fastapi). 
Aggrepapper be default aggregates news from two different External APIs, 
[News API](https://newsapi.org/), and [Reddit](https://www.reddit.com/dev/api/). 
Moreover, our implementation is inhancedwith [Redis](https://redis.io/) 
as a chaching system that works by temporarily storing information in 
a key-value data structure, which we set it to expire after 1 hour in 
case new news articles got published.

## Table Of Contents

The documentation consists of two separate parts:

1. [How-To Guides](how-to-guides.md)
2. [Explanation And References](reference_explaination.md)

Quickly find what you're looking for depending on
your use case by looking at the different pages.

## GitHub
You can find the code of the course in this github 
[repo](https://github.com/ammarkarkour/aggrepapper). The repo contains 
information about how to get the code and how to run the application.

