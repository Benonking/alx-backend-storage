#!/usr/bin/env python3
'''
Implement get_page function: get HTML from requets and returns it
'''
import requests
from typing import Callable
import redis

# connect to redis server
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)


# decorator to cache result in redis
def chached_get_page(func: Callable) -> Callable:
    '''
    run wrapper when get_page is called
    '''
    def wrapper(url):
        '''
        check if page is cached in Redis
        '''
        cached_html = redis_client.get(url)
        if cached_html is not None:
            # increment the access count and return the cached ttml content
            redis_client.incr(f"count:{url}")
            return cached_html.decode('utf-8')

        # if not cached , make HTTP request
        res = requests.get(url)

        if res.status_code == 200:
            # cache the html content with access count and HTML contnent
            redis_client.set(url, res.text, ex=10)
            redis_client.incr(f"count:{url}")
            return res.text
        else:
            return f"Failed to retrieve the page"
    return wrapper


# Decorator to cache the result
@chached_get_page
def get_page(url: str) -> str:
    '''
    get HTML page from URL and return it
    '''
    return url


if __name__ == "__main__":

    url = "http://slowwly.robertomurray.co.uk"
    get_page(url)