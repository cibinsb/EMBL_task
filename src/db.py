import time
import mysql.connector as connector
from mysql.connector import Error as DBError
from helper.utils import Constants
from helper.log import logger
#from dataclasses import dataclass

#@dataclass(order = True)
class DataBase:
    def __init__(self,reconnect):
        self.reconnect=reconnect
        self.connection = None
        self.cursor = None
        self.connect()
        self.init_cursor()

    def connect(self,retry_counter=0):
        if not self.connection:
            try:
                self.connection = connector.connect(host=Constants.host.value, user=Constants.user.value,
                                                    database=Constants.database.value,
                                                    pool_size=Constants.pool_size.value,
                                                    connect_timeout=3)
                retry_counter = 0
                return self.connection
            except DBError as error:
                if not self.reconnect or retry_counter >= Constants.limit_retries.value:
                    raise error
                else:
                    retry_counter += 1
                    logger.info("DB Connection error {}. reconnecting {}".format(str(error).strip(), retry_counter))
                    time.sleep(5)
                    self.connect(retry_counter)
            except (Exception, DBError) as error:
                raise error

    def get_data(self, query,retry_counter = 0) -> []:
        try:
            self.cursor.execute(query)
            retry_counter = 0
        except DBError as error:
            if retry_counter >= Constants.limit_retries.value:
                raise error
            else:
                retry_counter += 1
                logger.info("DB Connection error {}. retrying {}".format(str(error).strip(), retry_counter))
                time.sleep(1)
                self.reset()
                self.get_data(query, retry_counter)
        columns = tuple([col[0] for col in self.cursor.description])
        data=[dict(zip(columns, row)) for row in self.cursor]
        return data

    def reset(self):
        self.disconnect()
        self.connect()
        self.init_cursor()

    def init_cursor(self):
        if not self.cursor or self.cursor.closed:
            if not self.connection:
                self.connect()
            self.cursor = self.connection.cursor()
            return self.cursor

    def disconnect(self):
        if self.connection:
            if self.cursor:
                self.cursor.close()
            self.connection.close()
            logger.info("MYSQL connection is closed")
        self.connection = None
        self.cursor = None

