#!/usr/bin/env python3
'''
    Define function to update mongo db
'''
import pymongo


def update_topics(mongo_collection, name, topics):
    '''
        update mongo database to change all topics of school(doc) based on name
        Args:
            name: school name to update
            topics: list of string to th list of topics approached in school
            mongo_collection: pymongo collection object
    '''
    mongo_collection.update(
        {"name": name},
        {"$set": {"topics": topics}}
        )
