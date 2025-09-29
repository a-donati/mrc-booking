
class Vessels:
    def __init__(self, name, cost_per_hour):
        self.name = name
        self.cost_per_hour = cost_per_hour

    def __str__(self):
        return f"{self.vessel_id}: {self.name} {self.cost_per_hour} cost per hour"

    def __repr__(self):
        return f"{self.vessel_id}: {self.name} {self.cost_per_hour} cost per hour"
    
