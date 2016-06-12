import mysql.connector
from SentimentAnalysis.Utility.DelimitedFileHelper import DelimitedFileHelper


class BaseDAO(object):
    def __init__(self, flat_file_path=None, sql=None):
        self._delimited_file_helper = None
        self._sql_cnx = None
        self._sql_db = None

        if flat_file_path is not None:
            self._delimited_file_helper = DelimitedFileHelper(flat_file_path)

        if sql is not None:
            self._sql_cnx = mysql.connector.connect(
                user=sql.usr,
                password=sql.passwd,
                host=sql.host,
                database=sql.db)
            self._sql_db = sql.db

