#!/usr/bin/env python3
'''
    Define Function schools_by_topic
    Return a list of schools with a specific topic
'''
import pymongo


def schools_by_topic(mongo_collection, topic):
    '''
        search collectiona and retun documents in mongo db with certain tiopic
        Args:
            topic: string to be searched
            mongo_collection: pymongo collection object
    '''
    return [topic for topic in mongo_collection.find({"topics": topic})]
