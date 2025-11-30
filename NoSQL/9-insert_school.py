#!/usr/bin/env python3
"""task 9"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """insert function"""

    s = mongo_collection.insert_one(kwargs)
    return s.inserted_id
