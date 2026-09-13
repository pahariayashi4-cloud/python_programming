class Transport:

    def __init__(self, type):
        self.type = type

    def show(self):
        print("Type of Transport:", self.type)


class Boat(Transport):

    def __init__(self, type, capacity, source, destination):
        super().__init__(type)
        self.capacity = capacity
        self.source = source
        self.destination = destination

    def show(self):
        print("----- Boat Details -----")
        print("Type:", self.type)
        print("Capacity:", self.capacity)
        print("Source:", self.source)
        print("Destination:", self.destination)


class Bus(Transport):

    def __init__(self, type, seat_no, source, destination):
        super().__init__(type)
        self.seat_no = seat_no
        self.source = source
        self.destination = destination

    def show(self):
        print("----- Bus Details -----")
        print("Type:", self.type)
        print("Seat No:", self.seat_no)
        print("Source:", self.source)
        print("Destination:", self.destination)


boat1 = Boat("Boat", 100, "Kolkata", "Haldia")
boat2 = Boat("Boat", 150, "Goa", "Mumbai")


bus1 = Bus("Bus", 25, "Kolkata", "Durgapur")
bus2 = Bus("Bus", 40, "Delhi", "Agra")

boat1.show()
print()

boat2.show()
print()

bus1.show()
print()

bus2.show()