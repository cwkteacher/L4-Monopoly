class Space:
    def __init__(self,name):
        self.name = name

class Property:
    def __init__(self, name, cost, rent):
        self.name = name
        self.cost = cost
        self.rent = rent
        self.owner = "none"
        
class Player:
    def __init__(self, name):
        self.name = name
        self.money = 600
        self.position = 0