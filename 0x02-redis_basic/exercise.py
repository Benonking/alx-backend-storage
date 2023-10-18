#!/usr/bin/env python3
'''
Module defines a class cache
'''


import redis
from uuid import uuid4
from typing import Union, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.incr(key)
        result = method(self, *args, **kwargs)
        return result
    return wrapper


def replay(method: Callable):
    """replay function"""
    key = method.__qualname__
    inputs = key + ":inputs"
    outputs = key + ":outputs"
    redis = method.__self__._redis
    count = redis.get(key).decode("utf-8")
    print(f"{key} was called {count} times:")
    in_list = redis.lrange(inputs, 0, -1)
    out_list = redis.lrange(outputs, 0, -1)
    redis_zipped = list(zip(in_list, out_list))
    for a, b in redis_zipped:
        attr, result = a.decode("utf-8"), b.decode("utf-8")
        print(f"{key}(*{attr}) -> {result}")


def call_history(method: Callable) -> Callable:
    '''store history of inputs and outputs for a function'''
    key = method.__qualname__
    inputs = key + ":inputs"
    outputs = key + ":outputs"

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        '''wrapper func'''
        self._redis.rpush(inputs, str(args))
        res = method(self, *args, **kwargs)
        self._redis.rpush(outputs, str(res))
        return res
    return wrapper


class Cache:
    '''
        define class whic initialises init method with private varibale
        Define calss store to store strin in a redis db
    '''
    def __init__(self, host='localhost', port=6379, db=0):
        '''
        Initialse class with private varible whic is an instance of redis
        '''
        self._redis = redis.Redis(host=host, port=port, db=db)
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''
            store data in redis with value of Arg:data
            Return str (key)
        '''
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key, fn: Callable[[bytes], Union[str, int, float]] = None):
        val = self._redis.get(key)
        if val is not None and fn is not None:
            return fn(val)
        return val

    def get_str(self, key):
        return self.get(key, fn=lambda val: val.decode('utf-8'))

    def get_int(self, key):
        return self.get(key, fn=lambda val: int(val))
