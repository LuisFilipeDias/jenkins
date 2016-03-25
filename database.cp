"""
    	This is the Database object.
    	It handles the sqlite-related operations

    	Luis Filipe Ribeiro Dias
              DTV Research
                   2016
"""
import sqlite3

class DB(object):
    """
        the class of the database object.
    """

	def __init__(self, host):
        """
            the initializer

        :param host
        :param user
        :param password
        :param db_name
        """
        self.host = host
        self.connection = None;

    def connect(self):
    """
            connect to the database, and
            hold the connection under the self.d_b
    """
        self.connection = sqlite3.connect(self.host)

    def insert(self, table, name, field, value):
    """
        write to database a specific field,
        for specific entry (name)
        on specific table

    :param table:
    :param value:
    :param field:
    :param name:
    """
        # if the entry(name) is available then update it
        if self.get_id(table, name) is not None:
            sql = 'UPDATE `%s` SET `%s`' \
                    '="%s", `added`=CURRENT_TIMESTAMP WHERE `name`="%s"' \
                    % (table, field, value, name)

        # otherwise create a new entry(name)
        else:
            sql = 'INSERT INTO `%s` (`%s`' \
                  ',`name`, `added`) VALUES ("%s","%s",CURRENT_TIMESTAMP)' \
                  % (table, field, value, name)
        self.d_b.cursor().execute(sql)
	# commit to save changes.
        self.d_b.commit()

	def get_id(self, table, name):
        """

            select information from
            table on database

        :param sel:
        :param table:
        :param name:
        """

        sql = 'SELECT id FROM %s WHERE `name`="%s"' % (table, name)
        with self.d_b.cursor() as cursor:
            cursor.execute(sql)
            for c in cursor:
                return c.get('id')

    	def get_table(self, table):
        	"""
            	select information from
            	table on database

        	:param sel:
        	:param table:
        	:param name:
        	"""
        	sql = 'SELECT * FROM %s' % table

        	with self.d_b.cursor() as cursor:
            cursor.execute(sql)

    	def create_table(self, table):
        """
            create a new table
            on database

        :param table:
        """
            with self.d_b.cursor() as cursor:
            	sql = 'CREATE TABLE %s (' \
                  '%s varchar(255) MEDIUMINT NOT NULL AUTO_INCREMENT,' \
                  '%s varchar(255) varchar(255) NOT NULL,' \
                  '%s varchar(255) varchar(255) NOT NULL,' \
                  '%s varchar(255) varchar(255) NOT NULL,' \
                  '%s varchar(255) varchar(255) NOT NULL,' \
                  '%s varchar(255) varchar(255) NOT NULL,' \
                  '%s varchar(255) varchar(255) NOT NULL,' \
                  '%s varchar(255) varchar(255) NOT NULL,' \
                  '%s varchar(255) varchar(255) NOT NULL,' \
                  ' PRIMARY KEY (id));' \
                  % (table, "id", "name", "feature_1", "feature_2", "feature_3",
                     "feature_4", "feature_5", "feature_6", "added")
           	cursor.execute(sql)
        	# commit to save changes.
        	self.d_b.commit()

    	def disconnect(self):
        	"""
            	disconnect from database
	        """
        	self.d_b.close()
