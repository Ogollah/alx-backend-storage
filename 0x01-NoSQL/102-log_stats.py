#!/usr/bin/env python3
"""
Log stats
"""

from pymongo import MongoClient


def get_total_logs_count(nginx_collection):
    """Returns the total number of logs in the Nginx collection."""
    return nginx_collection.count_documents({})


def get_method_counts(nginx_collection, methods):
    """Returns a dictionary with counts for each HTTP method in Nginx logs."""
    method_counts = {}
    for method in methods:
        req_count = nginx_collection.count_documents({'method': method})
        method_counts[method] = req_count
    return method_counts


def get_top_ips(server_collection, limit=10):
    """Returns a list of the top IPs based on the total number of requests."""
    pipeline = [
        {
            '$group': {'_id': "$ip", 'totalRequests': {'$sum': 1}}
        },
        {
            '$sort': {'totalRequests': -1}
        },
        {
            '$limit': limit
        },
    ]
    return list(server_collection.aggregate(pipeline))


def print_nginx_request_logs_stats(nginx_collection):
    """Prints statistics about Nginx request logs."""
    total_logs_count = get_total_logs_count(nginx_collection)
    print('{} logs'.format(total_logs_count))

    print('Methods:')
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    method_counts = get_method_counts(nginx_collection, methods)
    for method, req_count in method_counts.items():
        print('\t{}: {}'.format(method, req_count))


def print_top_ips_stats(server_collection):
    """Prints statistics about the top IPs in a collection."""
    print('Top IPs:')
    top_ips = get_top_ips(server_collection)
    for ip_info in top_ips:
        ip = ip_info['_id']
        ip_requests_count = ip_info['totalRequests']
        print('\t{}: {}'.format(ip, ip_requests_count))


def run():
    """Provides some stats about Nginx logs stored in MongoDB."""
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx
    server_collection = client.logs.server

    print_nginx_request_logs_stats(nginx_collection)
    print_top_ips_stats(server_collection)


if __name__ == '__main__':
    run()
