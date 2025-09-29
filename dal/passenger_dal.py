import mysql.connector


class PassengerDAL:
    def __init__(self, db_connection):
        self.db_connection = db_connection
    # Add passenger method

    def addPassenger(self, passenger_name, passenger_address, passenger_phone):
        cursor = self.db_connection.mydb.cursor()
        try:
            cursor.callproc("addPassenger", [
                            passenger_name, passenger_address, passenger_phone])
            self.db_connection.mydb.commit()
            return True, None
        except mysql.connector.Error as err:
            return False, str(err)
        finally:
            cursor.close()

    def getPassengerId(self, passenger_name):
        cursor = self.db_connection.mydb.cursor()
        cursor.execute(f"SELECT getPassengerId('{passenger_name}');")
        result = cursor.fetchall()
        cursor.close()
        return result[0][0]