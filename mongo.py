"""
Module for mongo connections
"""
import os
from pymongo import MongoClient

MONGO_HOST = os.environ['MONGO_HOST']
MONGO_PORT = os.environ['MONGO_PORT']
MONGO_USER = os.environ['MONGO_USER']
MONGO_PASSWORD = os.environ['MONGO_PASSWORD']


class Connection():
    """
    Class to make mongo connections
    """
    def __init__(self):
        self.mongo_uri = "mongodb://%s:%s@%s:%s" % (
            MONGO_USER, MONGO_PASSWORD, MONGO_HOST, MONGO_PORT)
        self.connection = None

    def init_connection(self):
        """
        Starts mongo connection
        """
        self.connection = MongoClient(self.mongo_uri)

    def close_connection(self):
        """
        Close mongo connections
        """
        self.connection.close()

    @classmethod
    def with_connection(cls, wrapped):
        """
        Decorator function that provides mongo connection
        instance to its wrapped functions

        Argumments:
            wrapped:function
        """
        def connection(*args, **kwargs):
            """
            Open and close mongo connnection, executes wrapped function
            """
            connection_instance = cls()
            connection_instance.init_connection()
            result = wrapped(*args, **kwargs, mongo_connection=connection_instance.connection)
            connection_instance.close_connection()
            return result

        return connection
