#!/usr/bin/env python3
"""
provides some stats about Nginx logs stored in MongoDB
"""

from pymongo import MongoClient


def get_total_logs_count(collection):
    """Returns the total number of logs in the collection."""
    return collection.count_documents({})


def get_method_counts(collection, methods):
    """Returns a dictionary with counts for each HTTP method."""
    method_counts = {}
    for method in methods:
        req_count = collection.count_documents({'method': method})
        method_counts[method] = req_count
    return method_counts


def get_status_checks_count(collection):
    """Returns the count of status check logs."""
    return collection.count_documents({'method': 'GET', 'path': '/status'})


def print_nginx_request_logs(nginx_collection):
    """Prints stats about Nginx request logs."""
    total_logs_count = get_total_logs_count(nginx_collection)
    print(f'{total_logs_count} logs')

    print('Methods:')
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    method_counts = get_method_counts(nginx_collection, methods)
    for method, req_count in method_counts.items():
        print(f'\tmethod {method}: {req_count}')

    status_checks_count = get_status_checks_count(nginx_collection)
    print(f'{status_checks_count} status check')


def run():
    """Provides some stats about Nginx logs stored in MongoDB."""
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx
    print_nginx_request_logs(nginx_collection)


if __name__ == '__main__':
    run()
