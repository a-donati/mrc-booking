import mysql.connector

# config = {'user': 'root', 'password': 'db123456', 'database': 'mrc'}

booking_cache = []

class DBConnection():
    def __init__(self, config):
        self.config = config
        self.mydb = None
        self.connect()

    def connect(self):
        # Connect to the DB
        try:
            self.mydb = mysql.connector.connect(**self.config)
            print("Database connection established.")
        except mysql.connector.Error as err:
            print(f"Error connecting to the database: {err}")
            self.mydb = None

    def close(self):
        # Close the connection to the db
        if self.mydb:
            self.mydb.close()
            print("DB connection has been closed")








