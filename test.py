""" Module for make mongo connection tests """
from mongo import Connection

@Connection.with_connection
def list_databases(mongo_connection=None):
    """
    Get and print list database names
    """
    databases = mongo_connection.list_databases()
    for database in databases:
        print(database.get('name'))

if __name__ == "__main__":
    list_databases()
