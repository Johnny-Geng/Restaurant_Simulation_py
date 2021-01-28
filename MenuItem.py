# Johnny Geng, johnnyge@usc.edu

class MenuItem(object):
    def __init__(self, name, types, price, description):
        self.name = name
        self.types = types
        self.price = price
        self.description = description

    # Define Get Methods
    def getName(self):
        return self.name
    def getTypes(self):
        return self.types
    def getPrice(self):
        return self.price
    def getDescription(self):
        return self.description

    # Define the Message
    def __str__(self):
        myString = self.name + " (" + self.types + "): " + str(self.price) + "\n\t" + self.description
        return myString
