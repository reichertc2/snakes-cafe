appetizer_items = ["Appetizers", ["Wings", "Cookies", "Spring Rolls"]]
entree_items = ["Entree", ["Salmon", "Steak",
                           "Meat Tornado", "A Literal Garden"]]
dessert_items = ["Dessert", ["Ice Cream", "Cake", "Pie"]]
drink_items = ["Drinks", ["Coffee", "Tea", "Unicorn Tears"]]

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


def orderUp():
    order_request = input("> ").capitalize()
    if (order_request != "Quit"):
        print(f"** 1 order of {order_request} have been added to your meal **")
        order_request = input("> ")
    else:
        print("bye")


def initalPrompt():
    welcomeMessage()
    menuList(appetizer_items)
    menuList(entree_items)
    menuList(dessert_items)
    menuList(drink_items)
    orderPrompt()


initalPrompt()
orderUp()
