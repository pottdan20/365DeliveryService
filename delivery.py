import sys


from userController import checkIfUserExist , createUser, attemptLogin
from menuController import getMenuItems, getItemIdByName
from deliveryController import createDelivery, attemptToCancel, canRate, rateDelivery



def main():
        currentUser = None
        cart = []

        print("enter q to quit at any time")
        args = [0,0]
    # try:
        while args == None or args[0] != "q": #before 'continue' set args to None
            if(currentUser is None):
                args = input("login or signup? ").split(" ")
                if(args[0] == "signup"):
                    username = input("input email: ")
                    if checkIfUserExist(username):
                        print("this user exisit, try restarting and logging in")
                        args = None
                        continue
                    password = input("new password: ")
                    passConfirm = input("confirm password: ")
                    while(password != passConfirm):
                        print("passwords do not match...")
                        password = input("new password: ")
                        passConfirm = input("confirm password: ")
                    try:
                        currentUser = createUser(username,password)
                    except:
                        print("error creating user")
                        args = None
                        continue

                elif args[0] == "login":
                    username = input("email: ")
                    password = input("password: ")
                    try:
                        currentUser = attemptLogin(username, password)
                    except:
                        print("error: email or password are incorrect")
                        args = None
                        continue
                else:
                    print("invalid input")
                    args = None
                    continue
            
            # user is logged in for all code below
            
            args = input("Enter Command: ").split(" ")


            if args[0] == "menu": #list menu
                menuItems = getMenuItems()
                print(menuItems)
            elif args[0] == "add": # add item
                try:
                    itemName = args[1]
                    quant = int(args[2])
                except:
                    print("invalid input format: add [name of item] [count]")
                    args = None
                    continue

                try:
                    newItem = getItemIdByName(itemName)
                    newEntry = True
                    for i in cart:
                        if i.get("id") == newItem:
                            i["count"] +=  quant
                            newEntry = False
                    if newEntry:
                        cart.append({"id": newItem, "name": itemName, "count": quant})
                    print("added")
                except:
                    print("error adding to cart. retry")
                    args = None
                    continue
            elif args[0] == "remove":
                try:
                    itemName = args[1]
                    quant = int(args[2])
                except:
                    print("invalid input format: add [name of item] [count]")
                    args = None
                    continue

                try:
                    for i in range(0,len(cart)):
                        if cart[i].get("name") == itemName:
                            if(quant >=  cart[i].get("count")): #either adjusts the count of an item in cart or removes entierly
                                del cart[i]
                            else:
                                cart[i]["count"] -= quant
                    print("added")
                except:
                    print("error removing from. retry")
                    args = None
                    continue
            elif args[0] == "cart": #lists items in cart
                for i in cart:
                    print(i.get("name") + ": " + str(i.get("count")))
            elif args[0] == "checkout":
                if len(cart) == 0:
                    print("add an item to cart first")
                    continue
                try:
                    addr = input("delivery address: ")
                    deliveryId = createDelivery(currentUser, addr, cart)
                    presentAfterOrderOptions(deliveryId)
                except:
                    print("error checkingout. please try again")


def presentAfterOrderOptions(id):
    print("\n_____________________________")
    print("order placed...\nwait to rate this delivery or just leave and wait for arrival")
    print("please wait for arrival")
    while True:
        arg = input("[rate,leave]: ")
        if arg == "rate":
            try:
                if canRate(id):
                    try:
                        rate = float(input("rate order 0-5: "))
                        rateDelivery(id, rate)
                    except:
                        print("error. make sure rate is a number")
                        continue
                else:
                    print("sorry, you must recieve your order before rating the delivery...")
                    continue
                
            except:
                print("error rating...")
                continue
        elif arg == "leave" or arg == "q":
            break
        else:
            print("please enter valid command\n")
                
                
                
    # except Exception as e: print(e)

       


if __name__ == '__main__':
    main()
