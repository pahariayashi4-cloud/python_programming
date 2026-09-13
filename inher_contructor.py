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
        print("Boat Details")
        print("Type:", self.type)
        print("Capacity:", self.capacity)
        print("Source:", self.source)
        print("Destination:", self.destination)
        print()


class Bus(Transport):
    def __init__(self, type, capacity, seat_no, source, destination):
        super().__init__(type)
        self.capacity = capacity
        self.seat_no = seat_no
        self.source = source
        self.destination = destination

    def show(self):
        print("Bus Details")
        print("Type:", self.type)
        print("Capacity:", self.capacity)
        print("Seat Number:", self.seat_no)
        print("Source:", self.source)
        print("Destination:", self.destination)
        print()


boat1 = Boat("Water Transport", 50, "Kolkata", "Haldia")
boat2 = Boat("Water Transport", 80, "Kolkata", "Sundarbans")

bus1 = Bus("Road Transport", 40, 15, "Kolkata", "Digha")
bus2 = Bus("Road Transport", 50, 25, "Kolkata", "Siliguri")

boat1.show()
boat2.show()
bus1.show()
bus2.show()