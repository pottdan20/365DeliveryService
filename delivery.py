import sys


from userController import checkIfUserExist , createUser, attemptLogin
from menuController import getMenuItems, getItemIdByName




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
                    print(cart)
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

                # try:
                for i in range(0,len(cart)):
                    if cart[i].get("name") == itemName:
                        if(quant >=  cart[i].get("count")):
                            del cart[i]
                        else:
                            cart[i]["count"] -= quant
                print(cart)
                '''except:
                    print("error removing from. retry")
                    args = None
                    continue'''

                
                
    # except Exception as e: print(e)

       


if __name__ == '__main__':
    main()
