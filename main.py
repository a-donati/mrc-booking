from dal.mrc_dal import DBConnection  # Database connection class
from dal.passenger_dal import PassengerDAL  # Passenger Data Access Layer
from dal.vessels_dal import VesselsDAL  # Vessel Data Access Layer
from dal.trip_dal import TripsDAL  # Trips Data Access Layer
from models.passengers import Passengers  # Passenger model
from models.vessels import Vessels  # Vessel model
from models.trips import Trips  # Trip model
from datetime import datetime  # For date and time handling
from bll.mrc_bll import *

def main():
    try:
        # Prompt the user for credentials
        config = get_db_config()
        # Pass config credentials to the dal
        db_connection = DBConnection(config)
        # Check connection
        if not check_db_connection(db_connection):
            return

        # create bll instance
        bll = Bll(db_connection)

        total_revenue = bll.get_total_revenue()  # Retrieve total revenue data
        display_total_revenue(total_revenue)  # Display data

        vessel_id = bll.get_vessel_id("Sea Breeze")  # Retrieve vessel ID
        display_vessel_id("Sea Breeze", vessel_id)  # Display ID
        warrior_vessel_id = bll.get_vessel_id(
            "Warriors")  # (No Match)
        display_vessel_id("Warriors", warrior_vessel_id) # (No Match)

        # Add a trip
        trip_result = bll.add_trip(
            "Sea Breeze", "John Smith", "2025-04-01 13:00:00", 5, 6)
        # Unpack and display the add trip result
        display_new_trip_result(*trip_result)

        # Attempt to add another trip with a non-existing vessel and non-existing passenger
        trip2_result = bll.add_trip(
            "Periwinkle", "Arianka Grande", "2025-04-06 09:00:00", 3, 3)
        
        # Unpack and display the trip result
        display_new_trip_result(*trip2_result)

        # Display all trips
        bll.get_all_trips()

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
