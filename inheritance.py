##casestudy
#create a class transport  with a method getval() to initialise the varibale type of transport . define a method showval() to display the type of variable . create a subclass bus with th method input_val to initialise the variable seat_number , & source , destination .and
#define a method display() to show all the variables of bus



class Transport:
    def get_val(self):
        self.transport_type = input("enter:")

    def show(self):
        print("transport type:{self.transport_type}")

class Bus(Transport):
    def input_val(self):
        super().get_val()
        self.seat_no= int(input("enter seat no:"))
        self.source=input("enter source:")
        self.dest=input("enter dest:")

def display(self):
    self.show_val()
    print("seat no:" ,self.seat_no)
    print("source:",self.source)
    print("destination:",self.dest)

b=Bus()
b.input_val()
b.display()

#initialise variable of the class transport and the class bus with contructor

class Transport:
    def __init__(self, transport_type):
        self.transport_type = transport_type
    def show(self):
        print("Transport type:", self.transport_type)


class Bus(Transport):
    def __init__(self, transport_type, seat_no, source, dest):
        super().__init__(transport_type)
        self.seat_no = seat_no
        self.source = source
        self.dest = dest

    def display(self):
        self.show()
        print("Seat no:", self.seat_no)
        print("Source:", self.source)
        print("Destination:", self.dest)


transport_type = input("Enter transport type: ")
seat_no = int(input("Enter seat no: "))
source = input("Enter source: ")
dest = input("Enter destination: ")

b = Bus(transport_type, seat_no, source, dest)

b.display()