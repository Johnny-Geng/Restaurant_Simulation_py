# Johnny Geng, johnnyge@usc.edu

from MenuItem import MenuItem
class Menu(object):
    # a list of strings containing different types of items on the menu
    MENU_ITEM_TYPES = ["Drink", "Appetizer", "Entree", "Dessert"]

    # Create a dictionary:
    # keys are strings representing the types of the menu item,
    # and the values are a list of MenuItem objects.
    def __init__(self, fileName):
        self.menuItemDictionary = {}
        for o in self.MENU_ITEM_TYPES:
            self.menuItemDictionary[o] = []
        fileIn = open(fileName, "r")
        for line in fileIn:
            line = line.strip()
            dataList = line.split(",")
            myObject = MenuItem(dataList[0],dataList[1],dataList[2],dataList[3])
            if dataList[1] in self.MENU_ITEM_TYPES:
                self.menuItemDictionary[dataList[1]].append(myObject)
        fileIn.close()

    # Get the correct MenuItem from the dictionary using its type and index
    # position in the list of items.
    def getMenuItem(self, typeOfItem, indexPosition):
         answer = self.menuItemDictionary[typeOfItem][indexPosition]
         return answer

    # Print a header with the type of menu items, followed by a numbered list
    # of all the menu items of that type.
    def printMenuItemsByType(self, typeMenuItem):
        print()
        print("-----" + typeMenuItem + "-----")
        number = 0
        for i in self.menuItemDictionary.get(typeMenuItem):
            print(str(number) + ") " + str(i))
            number += 1

    # return an integer representing the number of MenuItems of the input type
    def getNumMenuItemsByType(self, x):
        return len(self.menuItemDictionary.get(x))