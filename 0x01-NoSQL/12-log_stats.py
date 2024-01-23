#!/usr/bin/env python3
"""
provides some stats about Nginx logs stored in MongoDB
"""

from pymongo import MongoClient


def nginx_logs_stats():
    """
    Provides statistics about Nginx logs stored in MongoDB.

    This function connects to the
    MongoDB database "logs" and collection "nginx",
    retrieves various statistics, and prints the results.

    Displayed Statistics:
    - Total number of logs
    - Number of logs for each HTTP method (GET, POST, PUT, PATCH, DELETE)
    - Number of logs with method=GET and path=/status

    Returns:
    None
    """
    # Connect to MongoDB
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
