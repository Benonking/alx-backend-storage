#!/usr/bin/env python3
'''
Module that defines a function to insert a doc in a mongo db
'''

import pymongo


def insert_school(mongo_collection, **kwargs):
    '''
        insert doc in collection based on **kwargs
        Args:
            mongo_collection
            **kwargs
    '''
    if len(kwargs) <= 0:
        return None
    return mongo_collection.insert(kwargs)
