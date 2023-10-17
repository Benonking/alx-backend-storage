#!/usr/bin/env python3
'''
Module 8-all
script List all documents in a mongo db 
'''

import pymongo

def list_all(mongo_collection):
  if not mongo_collection:
    return []
  
  return list(mongo_collection.find())
