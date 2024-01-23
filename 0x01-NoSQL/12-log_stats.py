#!/usr/bin/env python3
"""
provides some stats about Nginx logs stored in MongoDB
"""

from pymongo import MongoClient


def nginx_logs_stats():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["logs"]
    collection = db["nginx"]

    total_logs = collection.count_documents({})

    print(f"{total_logs} logs")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\t{method}: {count} logs")

    special_logs_count = collection.count_documents(
        {"method": "GET", "path": "/status"})
    print(f"{special_logs_count} logs with method=GET and path=/status")


if __name__ == "__main__":
    nginx_logs_stats()
