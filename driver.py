import sys
from userController import checkIfUserExist , createUser

def main():
    print("enter q to quit at any time")
    args = input("login or signup? ")
    try:
        while args[0] != "q":
            print(args)
            if(args == "signup"):
                username = input("input username: ")
                if checkIfUserExist(username):
                    print("this user exisit, try restarting and logging in")
                    continue
                password = input("new password: ")
                passConfirm = input("confirm password: ")
                while(password != passConfirm):
                    print("passwords do not match...")
                    password = input("new password: ")
                    passConfirm = input("confirm password: ")
                createUser(username,password)
            
            args = input("next?")
                
                
    except:
        print("error: ")


main()