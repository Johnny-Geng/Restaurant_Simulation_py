# Johnny Geng, johnnyge@usc.edu

from MenuItem import MenuItem
class Diner(object):
    # a list of strings containing the possible statuses a diner might have
    STATUSES = ["seated", "ordering", "eating", "paying", "leaving"]

    def __init__(self, nameOfDiner):
        self.name = nameOfDiner
        self.order = []
        self.status = 0

    # Define Get Methods
    def getName(self):
        return self.name

    def getOrder(self):
        return self.order

    def getStatus(self):
        return self.STATUSES[self.status]

    # Increase the diner’s status by 1
    def updateStatus(self):
        self.status += 1

    # Adds the menu item to the end of the list of menu items (instance attribute)
    def addToOrder(self, MenuItemObject):
        self.order.append(MenuItemObject)

    # Print a message containing all the menu items the diner ordered
    def printOrder(self):
        print()
        print(self.name + " ordered:")
        for n in self.order:
            print("- ", end=" ")
            print(n)

    # return a float representing the total cost of the diner’s meal
    # Total up the cost of each of the menu items the diner ordered.
    def calculateMealCost(self):
        money = 0
        for m in self.getOrder():
            money += float(m.getPrice())
        return money

    # Define the Message
    def __str__(self):
        msg = "Diner " + self.getName() + " is currently " + self.getStatus()
        return msg
