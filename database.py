"""
    This is the Database object.
    It handles the sqlite-related operations

    Luis Filipe Ribeiro Dias
            2016
"""
import sqlite3


class DB(object):
    """
        the class of the database object.
    """

    def __init__(self, database):
        """
            the initializer
        """
        self.connection = sqlite3.connect(database)

    def insert(self, table, cols, vals):
        """
            insert value into row
        """
        # lets assume we will only have 2 columns, for simplification
        assert len(cols) == len(vals) == 2
        cursor = self.connection.cursor()
        sql = "CREATE TABLE IF NOT EXISTS %s (%s, %s, added)" \
              % (table, cols[0], cols[1])
        cursor.execute(sql)
        sql = "INSERT INTO %s (%s, %s, added) VALUES " \
              "('%s','%s',CURRENT_TIMESTAMP)" \
              % (table, cols[0], cols[1], vals[0], vals[1])
        cursor.execute(sql)

        self.connection.commit()

    def __del__(self):
        self.connection.close()
