#!/usr/bin/env python3
"""
returns the list of school having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    list of school having a specific topic
    """
    matcher = {
        'topics': {
            '$eleMatch': {
                '$mtch': topic,
            },
        },
    }
    return [doc for doc in mongo_collection.find(matcher)]
