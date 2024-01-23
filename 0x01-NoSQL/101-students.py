#!/usr/bin/env python3
"""
returns all students sorted by average score:
"""


def top_students(mongo_collection):
    """
    Returns all students in a collection sorted by average score.

    Args:
    - mongo_collection: pymongo collection object

    Returns:
    - List of students with '_id', 'name', and 'averageScore'.
    """
    pipeline = [
        {
            '$project': {
                '_id': 1,
                'name': 1,
                'averageScore': {
                    '$avg': '$topics.score',
                },
            },
        },
        {
            '$sort': {'averageScore': -1},
        },
    ]

    students = mongo_collection.aggregate(pipeline)
    return list(students)
