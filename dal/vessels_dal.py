import mysql.connector

class VesselsDAL:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def getVesselID(self, vessel_name):
        cursor = self.db_connection.mydb.cursor()
        cursor.execute(f"SELECT getVesselId('{vessel_name}');")
        result = cursor.fetchall()
        cursor.close()
        return result[0][0]  # Return the first element of the first tuple

    def addVessel(self, name, cost_per_hour):
        cursor = self.db_connection.mydb.cursor()
        try:
            cursor.callproc("addVessel", [name, cost_per_hour])
            self.db_connection.mydb.commit()
            return True
        except mysql.connector.Error as err:
            print(f"Database Error: {err}")
            return False
        finally:
            cursor.close()

    def getTotalRevenue(self):
        cursor = self.db_connection.mydb.cursor()
        cursor.execute(f"SELECT * FROM TotalRevenuebyVessel;")
        result = cursor.fetchall()
        cursor.close()
        return result