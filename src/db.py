import mysql.connector as connector
from mysql.connector import Error as DBError
from helper.utils import Constants
from helper.log import logger


class DataBase:

    def __init__(self):
        try:
            self.conn = connector.connect(host=Constants.host.value, user=Constants.user.value,
                                          database=Constants.database.value)
        except DBError as err:
            raise Exception(err)

    def get_data(self, query):
        cursor = self.conn.cursor()
        try:
            cursor.execute(query)
        except DBError as ex:
            logger.info(ex)
            raise Exception(ex)
        columns = tuple([col[0] for col in cursor.description])
        return [dict(zip(columns, row)) for row in cursor]

    def disconnect(self):
        self.conn.close()
