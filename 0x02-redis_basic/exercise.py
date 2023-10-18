#!/usr/bin/env python3
'''
Module defines a class cache
'''


import redis
from uuid import uuid4
from typing import Union, Callable


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
