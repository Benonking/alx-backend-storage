#!/usr/bin/env python3
'''
Implement get_page function: get HTML from requets and returns it
'''
import requests
from typing import Callable
import redis
from functools import wraps

# connect to redis server
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)


# decorator to cache result in redis
def chached_get_page(func: Callable[[str], str]) -> Callable[[str], str]:
    '''
    run wrapper when get_page is called
    '''
    @wraps(func)
    def wrapper(url: str) -> str:
        '''
        check if page is cached in Redis
        '''
        redis_client.incr(f"count:{url}")
        cached_html = redis_client.get(url)
        
        if cached_html:
            # HTML contnent in cache
            return cached_html.decode('utf-8')

        # if not cached , make HTTP request
        res = func(url)

        # cache the html content with access count and HTML contnent
        redis_client.set(f"count:{url}", 0)
        redis_client.expire(url, 10)
        return res
    return wrapper


# Decorator to cache the result
@chached_get_page
def get_page(url: str) -> str:
    '''
    get HTML page from URL and return it
    '''
    return requests.get(url).text


if __name__ == "__main__":

    url = "http://slowwly.robertomurray.co.uk"
    get_page(url)
