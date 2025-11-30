#!/usr/bin/env python3
"""task 10 update"""
import mongo


def update_topics(mongo_collection, name, topics):
    """update function"""

    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
