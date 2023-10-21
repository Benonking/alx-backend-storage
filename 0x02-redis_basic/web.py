#!/usr/bin/env python3
'''
Implement get_page function: get HTML from requets and returns it
'''
import requests
from typing import Callable
import redis
from functools import wraps

# connect to redis server
redis_client = redis.Redis()


# decorator to cache result in redis
def chached_get_page(func: Callable) -> Callable:
    '''
    run wrapper when get_page is called
    '''
    @wraps(func)
    def wrapper(url: str) -> str:
        '''
        check if page is cached in Redis
        '''
        redis_client.incr(f"count:{url}")
        cached_html = redis_client.get(f'result:{url}')

        if cached_html:
            # HTML contnent in cache
            return cached_html.decode('utf-8')

        # if not cached , make HTTP request
        cached_html = func(url)
        # cache the html content with access count and HTML contnent
        redis_client.set(f"count:{url}", 0)
        redis_client.setex(f'cached_html:{url}', 10, cached_html)
        return cached_html
    return wrapper


# Decorator to cache the result
@chached_get_page
def get_page(url: str) -> str:
    '''
    get HTML page from URL and return it
    '''
    return requests.get(url).text
