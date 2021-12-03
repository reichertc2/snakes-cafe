APPETIZER_ITEMS = ["Appetizers", ["Wings", "Cookies", "Spring Rolls"]]
ENTREE_ITEMS = ["Entree", ["Salmon", "Steak",
                           "Meat Tornado", "A Literal Garden"]]
DESSERT_ITEMS = ["Dessert", ["Ice Cream", "Cake", "Pie"]]
DRINK_ITEMS = ["Drinks", ["Coffee", "Tea", "Unicorn Tears"]]

# found the method of lineBreak from LepordShark from StackOverflow


def lineBreak():
    for x in range(0, 37):
        print("*", end='', flush=True)
    print("*")


def centerText(text):
    print("**", end='', flush=True)
    str = text
    print(str.center(34), end='', flush=True)
    print("**")


def underlineText(text):
    text_length = len(text)
    for x in range(0, text_length - 1):
        print("-", end='', flush=True)
    print("-")


def welcomeMessage():
    lineBreak()
    centerText("Welcome to the Snakes Cafe!")
    centerText("Please see our menu below")
    centerText("")
    centerText("To quit at any time, type \"quit\"")
    lineBreak()
    print()


def menuList(array):
    print(f"{array[0]}")
    underlineText(array[0])
    array_length = len(array[1])
    for x in range(0, array_length):
        print(array[1][x])
    print()


def orderPrompt():
    lineBreak()
    centerText("What would you like to order?")
    lineBreak()

class Menu():
        def __init__(self, name, quantity = 0):
            self.name = name
            self.quantitiy = quantity

def populate_menu():
    menu_items = []
    for item in APPETIZER_ITEMS[1]:
       Menu([item])
    print(menu_items)


def orderUp():
    populate_menu()
    order_request = input("> ").capitalize()

    order = []
   

    if (order_request != "Quit"):
        print(f"** 1 order of {order_request} have been added to your meal **")
        order_request = input("> ")
    else:
        print("bye")



def initalPrompt():
    welcomeMessage()
    menuList(APPETIZER_ITEMS)
    menuList(ENTREE_ITEMS)
    menuList(DESSERT_ITEMS)
    menuList(DRINK_ITEMS)
    orderPrompt()


initalPrompt()
orderUp()
