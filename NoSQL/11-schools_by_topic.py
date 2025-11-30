#!/usr/bin/env python3
"""task 11 find"""
import pymongo


def schools_by_topic(mongo_collection, topic):
    """find function"""

    return list(mongo_collection.find({"topics": topic}))
