# Johnny Geng, johnnyge@usc.edu

from Menu import Menu
from Diner import Diner
class Waiter(object):
    def __init__(self, menu):
        self.diners = []
        self.menu = menu

    # Add the new Diner object to the waiter’s list of diners
    def addDiner(self, dinerObject):
        self.diners.append(dinerObject)

    # return an integer representing the number of diners the waiter is currently keeping track of
    def getNumDiners(self):
        return len(self.diners)

    # Print all the diners the waiter is keeping track of, grouped by their statuses
    # Loop through each of the possible dining statuses a Diner might have
    def printDinerStatuses(self):
        print()
        for num in range(0, 5):
            print("Diners who are " + Diner.STATUSES[num] + ":")
            for diner in self.diners:
                if diner.getStatus() == Diner.STATUSES[num]:
                    print("\tDiner " + diner.getName() + " is currently " + Diner.STATUSES[num])

    # Loop through the list of diners and check if the diner’s status is “ordering”
    # For each diner that is ordering, loop through the different menu types
    # With each menu type, print the menu items of that type, then
    # ask the diner to order a menu item by selecting a number
    # After the diner selected a menu item, add the item to the diner
    # Once the diner orders one menu item of each type, print the diner’s order
    def takeOrders(self):
        for diner in self.diners:
            if diner.getStatus() == "ordering":
                for number in range(0, 4):
                    item = Menu.MENU_ITEM_TYPES[number]
                    self.menu.printMenuItemsByType(item)

                    # Error check
                    error = True
                    while error:
                        try:
                            answer = int(input(diner.getName() + ", please select a " +
                                               item + " menu item number.\n>"))
                            if answer >= 0 and answer <= self.menu.getNumMenuItemsByType(item):
                                diner.addToOrder(self.menu.getMenuItem(item, answer))
                                error = False
                        except:
                            continue

                diner.printOrder()

    # Loop through the list of diners and check if the diner’s status is “paying”.
    # For each diner that is paying, calculate the diner’s meal cost and print it
    # out in a message to the diner.
    def ringUpDiners(self):
        for name in self.diners:
            if name.getStatus() == "paying":
                amount = str(name.calculateMealCost())
                print()
                print(name.getName() + ", your meal cost $" + amount)

    # Loop through the list of diners and check if the diner’s status is “leaving”.
    # For each diner that is leaving, print a message thanking the diner.
    # Loop through the list of diners backwards.
    # For each diner that is leaving, remove the diner from the list.
    def removeDoneDiners(self):
        leftDiner = []
        for a in self.diners:
            if a.getStatus() == "leaving":
                print()
                print(a.getName() + ", thank you for dining with us! Come again soon!")
                self.diners.remove(a)

    # This method allows the waiter to attend to the diners at their various
    # stages as well as move each diner on to the next stage
    def advanceDiners(self):
        self.printDinerStatuses()
        self.takeOrders()
        self.ringUpDiners()
        self.removeDoneDiners()
        for diner in self.diners:
            diner.updateStatus()
