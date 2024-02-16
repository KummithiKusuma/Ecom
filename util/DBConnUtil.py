# import psycopg2  # Assuming PostgreSQL database

# class DBConnUtil:
#     @staticmethod
#     def get_connection(connection_string: str):
#         # Establish a database connection and return the connection object
#         return psycopg2.connect(connection_string)


import psycopg2

class DBConnUtil:
    @staticmethod
    def get_connection(connection_string: str):
        # Establish a database connection and return the connection object
        return psycopg2.connect(connection_string)

# Define the connection string for PostgreSQL
connection_string = "dbname=LAPTOP-4P38AOPI\SESSIONINSTANCE user=your_username password=your_password host=your_host port=your_port"

# Call the static method to get a connection object
connection = DBConnUtil.get_connection(connection_string)
