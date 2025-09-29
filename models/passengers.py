
class Passengers:
    def __init__(self, passenger_name, passenger_address, passenger_phone):
        self.passenger_name = passenger_name
        self.passenger_address = passenger_address
        self.passenger_phone = passenger_phone
        # self.gets_sea_sick = gets_sea_sick

    def __str__(self):
        return f"{self.passenger_id}: {self.passenger_name} {self.passenger_address} {self.passenger_phone} {self.gets_sea_sick}"

    def __repr__(self):
        return f"{self.passenger_id}: {self.passenger_name} {self.passenger_address} {self.passenger_phone} {self.gets_sea_sick}"
