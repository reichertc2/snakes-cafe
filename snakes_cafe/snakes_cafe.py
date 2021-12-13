APPETIZER_ITEMS = ["Appetizers", ["Wings", "Cookies", "Spring Rolls"]]
ENTREE_ITEMS = ["Entree", ["Salmon", "Steak",
                           "Meat Tornado", "A Literal Garden"]]
DESSERT_ITEMS = ["Dessert", ["Ice Cream", "Cake", "Pie"]]
DRINK_ITEMS = ["Drinks", ["Coffee", "Tea", "Unicorn Tears"]]

menu_dict = dict({"Wings":0, "Cookies":0, "Spring Rolls":0,"Salmon":0, "Steak":0,"Meat Tornado":0, "A Literal Garden":0,"Ice Cream":0, "Cake":0, "Pie":0,"Coffee":0, "Tea":0, "Unicorn Tears":0})
# found the method of lineBreak from LepordShark from StackOverflow
order = []


def line_break():
    for x in range(0, 37):
        print("*", end='', flush=True)
    print("*")


def center_text(text):
    print("**", end='', flush=True)
    str = text
    print(str.center(34), end='', flush=True)
    print("**")


def underline_text(text):
    text_length = len(text)
    for x in range(0, text_length - 1):
        print("-", end='', flush=True)
    print("-")


def welcome_message():
    line_break()
    center_text("Welcome to the Snakes Cafe!")
    center_text("Please see our menu below")
    center_text("")
    center_text("To quit at any time, type \"quit\"")
    line_break()
    print()


def menu_list(array):
    print(f"{array[0]}")
    underline_text(array[0])
    array_length = len(array[1])
    for x in range(0, array_length):
        print(array[1][x])
    print()


def order_prompt():
    line_break()
    center_text("What would you like to order?")
    line_break()

    

def order_up():
    
    # print('menu_dict before order',menu_dict)
    order_request = input("> ").capitalize()
    order.append(order_request )
    # print('My Order', order)

    if (order_request != "Quit"):
        
        # print('order:', order_request)
        menu_dict[order_request] += 1
        print(f"** {menu_dict[order_request]} order of {order_request}(s) have been added to your meal **")
            # print('menu_dict after order',menu_dict)
        order_up()

    else:
        print("bye")



def inital_prompt():
    welcome_message()
    menu_list(APPETIZER_ITEMS)
    menu_list(ENTREE_ITEMS)
    menu_list(DESSERT_ITEMS)
    menu_list(DRINK_ITEMS)
    order_prompt()


inital_prompt()
order_up()
