class Human:
    def __init__(self, name="Human"):
        self.name = name
class Auto:
    def __init__(self, brand):
        self.brand = brand
        self.passengers = []
        
    def add_psseger(self, *args):
        for passengers in args:
            self.passengers.append(passengers)

    def print_passengers_names(self):
        if self.passengers != []:
            print(f"Names of {self.brand} passengers: ")
            for passengers in self.passengers:
                print(passengers.name)

        else :
            print(f"No passegners in {self.brand}")

nick = Human("Nick")
kate = Human("Kate")
car = Auto("BMW")
car.add_psseger(nick, kate)
car.print_passengers_names()