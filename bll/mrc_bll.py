from dal.vessels_dal import VesselsDAL
from dal.passenger_dal import PassengerDAL
from dal.trip_dal import TripsDAL
from models.vessels import Vessels
from models.passengers import Passengers
from models.trips import Trips
from dal.mrc_dal import DBConnection 
from datetime import datetime

class Bll:
    def __init__(self, db_connection):
        # Initialize DAL instances
        self.vessels_dal = VesselsDAL(db_connection)
        self.passengers_dal = PassengerDAL(db_connection)
        self.trips_dal = TripsDAL(db_connection)
    
    # Add Passenger
    def add_passenger(self, name, address, phone):
        if not all([name, address, phone]):  # Check if all arguments are provided
            return False, "All fields (name, address, phone) are required."

        # Handle invalid types
        if not isinstance(name, str) or not isinstance(address, str) or not isinstance(phone, str):
            return False, "Name, address, and phone must be strings."

        # Check if the passenger ID already exists
        passenger_id_exists = self.get_passenger_id(name)
        if passenger_id_exists == -1:  # Passenger does not exist
            success, error_message = self.passengers_dal.addPassenger(
                name, address, phone)
            return success, error_message  # Return the success and error message
        else:
            return False, "Passenger already exists."
    
    # Get passenger ID
    def get_passenger_id(self, name):
        return self.passengers_dal.getPassengerId(name)
    
    # Add vessel
    def add_vessel(self, name, cost_per_hour):
        vessel = Vessels(name, cost_per_hour)
        return self.vessels_dal.addVessel(vessel)
    
    # Get vessel ID
    def get_vessel_id(self, vessel_name):
        vessel_id = self.vessels_dal.getVesselID(vessel_name)
        return vessel_id if vessel_id is not None else -1
    
    
    def add_trip(self, vessel_name, passenger_name, date_and_time, length_of_trip, total_passengers):
    # Check if vessel exists
        vessel_id = self.get_vessel_id(vessel_name)

        # If vessel doesn't exist, create it using the stored procedure
        if vessel_id == -1:
            self.vessels_dal.addVessel(vessel_name, cost_per_hour=0)  # Using a default cost per hour

        # Check if passenger exists
        passenger_id = self.get_passenger_id(passenger_name)

        # If passenger doesn't exist, create it using the existing method
        if passenger_id == -1:
            self.add_passenger(passenger_name, address='Placeholder Address', phone='1234567890')  # Example data

        # Call the addTrip procedure
        result = self.trips_dal.addTrip(vessel_name, passenger_name, date_and_time, length_of_trip, total_passengers)

        # Handle the result
        if isinstance(result, tuple) and not result[0]:  # Check if entry failed
            return False, result[1]  # Return the SQL error message
        # elif result == -3:
        #     return False, "Both vessel and passenger not found."
        # elif result == -2:
        #     return False, "Passenger not found."
        # elif result == -1:
        #     return False, "Vessel not found."
        else:
            return True, result  

    # Get total revenue for vessels
    def get_total_revenue(self):
        total_revenue = self.vessels_dal.getTotalRevenue()
        return total_revenue
    
    # Get all trips and call display_all_trips()
    def get_all_trips(self):
        all_trips = self.trips_dal.getAllTrips()
        display_all_trips(all_trips)

# Display all trips
def display_all_trips(all_trips):
    if all_trips:
        print("\nDisplaying All Trips\n")
        print(f"{'Date and Time':<25} {'Length of Trip (hrs)':<20} {'Vessel Name':<20} {'Passenger Name':<20} {'Address':<40} {'Phone':<15} {'Total Passengers':<20} {'Cost':<10}")  # Headings
        print("-" * 150)  # Separator line

        for row in all_trips:
            # Unpack the rows
            date_and_time, length_of_trip, vessel_name, passenger_name, address, phone, total_passengers, cost = row

            # Format date_and_time
            if isinstance(date_and_time, datetime):
                date_and_time = date_and_time.strftime("%Y-%m-%d %H:%M:%S")

            print(f"{date_and_time:<25} {length_of_trip:<20} {vessel_name:<20} {passenger_name:<20} {address:<40} {phone:<15} {total_passengers:<20} {cost:<10}")
    else:
        print("No trips data available.")

    # Display total revenue
def display_total_revenue(total_revenue):
    if total_revenue:
        print("\n Total Revenue By Vessel \n")
        # Print the header
        print(f"{'Vessel Name':<20} {'Total Revenue':<15}")
        print("-" * 35)  # Separator line

        for row in total_revenue:
            vessel_name, revenue = row
            print(f"{vessel_name:<20} {revenue:<15}")
    else:
        print("No revenue data available.")

    # Display retrieved vessel ID
def display_vessel_id(vessel_name, vessel_id):
    if vessel_id == -1:
        print(f"Vessel {vessel_name} was not found.")
    else:
        print(f"{vessel_name} Vessel ID: {vessel_id}")
    
    # Display retrieved passenger ID
def display_passenger_id(passenger_name, passenger_id):
    if passenger_id == -1:
        print(f"Passenger {passenger_name} was not found.")
    else:
        print(f"{passenger_name} Passenger ID: {passenger_id}")
    
    # Display success/error message when adding passenger
def display_add_passenger_result(success, error_message):
    if success:
        print("Passenger added successfully.")
    else:
        print(f"Failed to add passenger: {error_message}")
    
    # Display success/error message when adding a new trip
def display_new_trip_result(success, error_message):
    if success:
        print("Trip added sucessfully.")
    else:
        print(f"Failed to add trip. '{error_message}'")
    
    # Prompt user for DB info
def get_db_config():
    print("Welcome to MRC Booking App")
    return {
        'user': input("Enter database username: "),
        'password': input("Enter database password: "),
        'database': input("Enter database name: ")
    }
    # Check the connection
def check_db_connection(db_connection):
    # Check if connection was successful
    if db_connection.mydb is None:
        print("Failed to connect to the database")
        return False
    return True

