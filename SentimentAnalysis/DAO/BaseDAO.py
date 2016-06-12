import mysql.connector
from SentimentAnalysis.Utility.DelimitedFileHelper import DelimitedFileHelper


class BaseDAO(object):
    def __init__(self, flat_file_path=None, sql=None):
        self.delimited_file_helper = None
        self.sql_cnx = None
        self.sql_db = None

        if flat_file_path is not None:
            self.delimited_file_helper = DelimitedFileHelper(flat_file_path)

        if sql is not None:
            self.sql_cnx = mysql.connector.connect(
                user=sql.usr,
                password=sql.passwd,
                host=sql.host,
                database=sql.db)
            self.sql_db = sql.db

