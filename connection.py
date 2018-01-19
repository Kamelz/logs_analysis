#!/usr/bin/env python3

import psycopg2


class DB():
    """
    'DB'  A database class to communicate with your stored data.
    Attributes:
        database: database name.
        user: user name.
        host: host name.
    """
    def __init__(self, table, user, host):
        """Inits DB class and sets the database paramters."""
        self.table = table
        self.user = user
        self.host = host
        self.conf = """dbname='%s'
        user='%s' host='%s'""" % (self.table, self.user, self.host)
        self.db_cursor = self.db_connect()

    def db_connect(self):
        """Connect to the database."""
        try:
            connection = psycopg2.connect(self.conf)
            return connection.cursor()
        except:
            print("I am unable to connect to the database")

    def query(self, query):
        """
        Executes the query and returns the result.
        Attributes:
            'query': the query string.
        """
        self.db_cursor.execute(query)
        return self.db_cursor.fetchall()

    def display_query_result(self, rows):
        """
        Displays the fetched rows.
        Attributes:
            'rows': array of a query result.
        """
        for row in rows:
            print(row)
