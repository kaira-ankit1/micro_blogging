import mysql.connector.pooling
from utils.util import readConfig

class Connection:
    connectioPool = None
    @staticmethod
    def createDBConnectionPool():
        config = readConfig()
        Connection.connectioPool = mysql.connector.pooling.MySQLConnectionPool(user=config.get('DB', 'USER'), 
                                  password=config.get('DB', 'PASSWORD'),
                                  host=config.get('DB', 'HOST'),
                                  database=config.get('DB', 'DB_NAME'),
								  pool_name = config.get('DB', 'POOL_NAME'),
                                  pool_size = int(config.get('DB', 'POOL_SIZE')))
        return Connection.connectioPool

    @staticmethod		
    def getConnection():
        if(Connection.connectioPool is None):
            Connection.createDBConnectionPool()
        return Connection.connectioPool.get_connection()
		    