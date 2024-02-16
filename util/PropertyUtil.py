from util.DBPropertyUtil import DBPropertyUtil
from util.DBConnUtil import DBConnUtil

class PropertyUtil:
    @staticmethod
    def get_connection():
        # Get connection properties from a property file
        connection_string = DBPropertyUtil.get_property_string("db.properties")
        # Establish a database connection and return the connection object
        return DBConnUtil.get_connection(connection_string)
