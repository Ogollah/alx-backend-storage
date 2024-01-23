#!/usr/bin/env python3
"""
returns the list of school having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns a list of schools with a specific topic from a MongoDB collection.

    Args:
    - mongo_collection: pymongo collection object
    - topic: string, the topic to search

    Returns:
    - List of schools with the specified topic.
    """
    query = {"topics": {"$in": [topic]}}
    result = mongo_collection.find(query)

    schools = [school for school in result]
    return schools
