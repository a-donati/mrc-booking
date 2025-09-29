import mysql.connector

class TripsDAL:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def getAllTrips(self):  # View - getAllTrips
        cursor = self.db_connection.mydb.cursor()
        cursor.execute("SELECT * FROM AllTrips;")
        result = cursor.fetchall()
        cursor.close()
        return result
    
    def addTrip(self, vessel_name, passenger_name, date_and_time, length_of_trip, total_passengers):
        cursor = self.db_connection.mydb.cursor()
        try:
            cursor.callproc("addTrip", [
                vessel_name, passenger_name, date_and_time, length_of_trip, total_passengers])
            self.db_connection.mydb.commit()

            # Check for output parameters or return values
            for result in cursor.stored_results():
                return result.fetchone()[0]

            return 1  # Default to success if no results are returned
        except mysql.connector.Error as err:
            return False, str(err)  # Return the error message directly
        finally:
            cursor.close()
