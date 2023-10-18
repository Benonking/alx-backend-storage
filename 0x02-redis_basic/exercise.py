#!/usr/bin/env python3
'''
Module defines a class cache
'''


import redis
from uuid import uuid4


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

    def store(self, data: [str, bytes, int, float]) -> str:
        '''
            store data in redis with value of Arg:data
            Return str (key)
        '''
        key = str(uuid4())
        self._redis.set(key, data)
        return key
