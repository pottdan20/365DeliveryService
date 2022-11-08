import sys
import sqlalchemy
import urllib.parse
import os
  from dotenv import load_dotenv

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
       
    # Load env file
    load_dotenv()

    # Connection Parameters (you will sub in with your own databases values)
    escapedPassword = urllib.parse.quote_plus(os.environ.get("DB_PASSWORD"))
    sqldialect = os.environ.get("DB_DIALECT")
    username = os.environ.get("DB_USER")
    database = os.environ.get("DB_NAME")
    host = os.environ.get("DB_HOST")

    # Build the connection string based on database specific parameters
    connectionString = f"{sqldialect}://{username}:{escapedPassword}@{host}/{database}"

    # Create a new DB engine based on our connection string
    engine = sqlalchemy.create_engine(connectionString)

    # Create a single connection to the database. Later we will discuss pooling connections.
    conn = engine.connect()

    # The sql we want to execute
    sql = """
    show tables
    """

    # Run the sql and returns a CursorResult object which represents the SQL results
    result = conn.execute(sqlalchemy.text(sql))

    # Iterate over the CursorResult object row by row and just print.
    # In a real application you would access the fields directly.
    for row in result:
        print(row)


if __name__ == '__main__':
    main()
