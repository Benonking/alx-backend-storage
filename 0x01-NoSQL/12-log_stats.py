#!/usr/bin/env python3
'''
  Script that provides stats about Nginx logs stored in MongoDb
  '''
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_logs = client.logs.nginx
    
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
   
    print(nginx_logs.count_documents() + "logs")
    print("Methods:")
    for method in methods:
        count: nginx_logs.count_documents({"method": method})
        print("\tmethod "+ method + ": "+count)
    status = nginx_logs.count_documents(
        {"method": "GET", "pat":"/status"}
        )
    print("status_get"+ status)
