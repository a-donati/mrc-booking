
class Trips:
    def __init__(self, vessel_id, passenger_id, dateandtime, length_of_trip, total_passengers):
        self.vessel_id = vessel_id
        self.passenger_id = passenger_id
        self.dateandtime = dateandtime
        self.length_of_trip = length_of_trip
        self.total_passengers = total_passengers

    def __str__(self):
        return f"{self.vessel_id} {self.passenger_id} {self.dateandtime} {self.length_of_trip} {self.total_passengers}"

    def __repr__(self):
        return f"{self.vessel_id} {self.passenger_id} {self.dateandtime} {self.length_of_trip} {self.total_passengers}"
