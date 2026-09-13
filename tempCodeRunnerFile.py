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