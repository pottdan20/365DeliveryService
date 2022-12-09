import sys
import time    

from userController import checkIfUserExist , createUser, attemptLogin
from menuController import getMenuItems, getItemIdByName
from deliveryController import orderStatus, createDelivery, attemptToCancel, canRate, rateDelivery, tipDelivery, getTip
from driverController import getAllAvailableDeliveries, checkActive,checkIfDeliveryExist, pickupDelivery, completeDelivery, validPickupDelivery


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
                    except Exception as e: 
                        print(e)
                        print("error: email or password are incorrect")
                        args = None
                        continue
                else:
                    print("invalid input")
                    args = None
                    continue
            
            # user is logged in for all code below
            
            args = input("Enter Command: ").split(" ")
            if(args[0] == "help"):
                print("Commands:\nmenu\ncart\nadd [item] [count]\nremove [item] [count]\ncheckout\nclockin")
            elif args[0] == "menu": #list menu
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
                    if newItem is None:
                        print("must be a valid item name")
                        continue
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
                    try:
                        for i in range(0,len(cart)):
                            if cart[i].get("name") == itemName:
                                if(quant >=  cart[i].get("count")): #either adjusts the count of an item in cart or removes entierly
                                    cart.pop(i)
                                else:
                                    cart[i]["count"] -= quant
                        print("removed")
                    except:
                        print("error removing from. retry")
                        args = None
                        continue
                except:
                    print("invalid input format: remove [name of item] [count]")
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
                    cart = []
                except Exception as e: 
                    print(e)
                    print("error checkingout. please try again")
            elif args[0] == "clockin":  # Enter Driver Mode 
                driverMode(currentUser, args) 


def driverMode(UId, args):
    current_time = time.strftime('%Y-%m-%d %H:%M:%S')

    print("----------------Driver Mode----------------")
    print(f"\nClocked in at: {current_time}")
    
    print("\nAvailable deliveries:")
    open_deliveries = getAllAvailableDeliveries()
    for delivery in open_deliveries:
        print(f"\nDId: {delivery[0]}")
        print(f"Pickup Location: {delivery[4]}")
        print(f"Dropoff Location: {delivery[5]}")

    print("\nCommands:")
    print("\trefresh")
    print("\tpickup [Did]")
    print("\tcomplete")
    print("\tclockout")

    while args[0] != "q":  # Driver mode loop
        args = input("[refresh, pickup [DId], complete, clockout]: ").split(" ")
        if args[0] == "refresh":  # print out all available deliveries
            print("Available deliveries:")
            open_deliveries = getAllAvailableDeliveries()
            for delivery in open_deliveries:
                print(f"\nDId: {delivery[0]}")
                print(f"PickupLocation: {delivery[4]}")
                print(f"DropoffLocation: {delivery[5]}")

        elif args[0] == "pickup" and len(args) == 2:  
            DId = args[1]
            if checkIfDeliveryExist(DId) and validPickupDelivery(DId):
                pickupDelivery(UId, DId)
            else:  # pickup failed - still stay in Driver Mode
                print("Invalid DId. Try another DId.")  
                continue

            arg = ""
            currTip = 0
            active = True
            while arg != "q" and active:  
                print("Current tip: $" + str(currTip))

                arg = input("[complete], any button to refresh: ")  # Driver must complete delivery
                
                if arg == "complete":
                    completeDelivery(DId)
                    print("Thanks for completing a delivery!")
                    break
                elif arg != "q":
                    try:
                        currTip = getTip(DId)
                        active = checkActive(DId)
                        if(not active):
                            print("\nORDER HAS BEEN CANCELED!!!\n")
                        else:
                            print("Order Is Active")
                    except:
                        print("error getting tip")
                        
        elif args[0] == "complete":
            print("Delivery not picked up yet. Pickup a delivery, refresh or quit.")

        elif args[0] == "clockout":  # exit Driver Mode
            current_time = time.strftime('%Y-%m-%d %H:%M:%S')
            print(f"Clocked out at: {current_time}")
            break
    


def presentAfterOrderOptions(id):
    print("\n________________________________________________ ")
    print("\n----------------- ORDER PLACED ----------------- ")
    print("please wait for arrival")
    while True:
        arg = input("[leave, status, cancel order, rate, tip]: ")
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
        elif arg == "tip":
            try:
                tip = float(input("tip amount: $"))
                tipDelivery(id, tip)
                print("adding $" + str(tip) + " tip")
            except Exception as e: 
                print(e)
                continue
        elif arg == "status":
            try:
                print("Status: " + orderStatus(id))
            except Exception as e: 
                print(e)
        elif arg == "cancel" or arg == "cancel order":
            try:
                if not attemptToCancel(id): #attempt to cancel is true if canceled before order is done
                    print("order has already been delivered.\n")
                    
                else:
                    print("canceled... goodbye\n\n\n")
                    break
            except:
                print("error canceling order...")

        elif arg == "leave" or arg == "q":
            cart
            break
        else:
            print("please enter valid command\n")
                
                
                
    # except Exception as e: print(e)

       


if __name__ == '__main__':
    main()
