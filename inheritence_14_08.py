# Create a class transport with a method getval() to initialize the variable type of transport (i.e Water or road or railway).
# Define a method show to print the type
# Create a child class Bus with the method input_val() to initialize the variable seat no and source , destination.
# Define a method display() to show all the variables of the bus.

class Transport:
    def getval(self):
        self.type = input("Enter type of transport: ")

    def show(self):
        print("Type of Transport:", self.type)

class Bus(Transport):
    def input_val(self):
        self.seat_no = int(input("Enter seat number: "))
        self.source = input("Enter source: ")
        self.destination = input("Enter destination: ")

    def display(self):
        self.show()
        print("Seat Number:", self.seat_no)
        print("Source:", self.source)
        print("Destination:", self.destination)

b = Bus()

b.getval()
b.input_val()
b.display()

# Initialize the variables of the class Transport and class bus with Constructor.

class Transport:
    def __init__(self, type):
        self.type = type

    def show(self):
        print("Type of Transport:", self.type)

class Bus(Transport):
    def __init__(self, type, seat_no, source, destination):
        super().__init__(type)
        self.seat_no = seat_no
        self.source = source
        self.destination = destination

    def display(self):
        self.show()
        print("Seat Number:", self.seat_no)
        print("Source:", self.source)
        print("Destination:", self.destination)

b = Bus("Road", 25, "Kolkata", "Durgapur")

b.display()
