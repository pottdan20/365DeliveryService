import sqlalchemy
import urllib.parse
import os
from dotenv import load_dotenv

main_connection = None


def get_connection():
    if main_connection:
        return main_connection
    else:
        return create_connection()


def create_connection():
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
    main_connection = engine.connect()
    

    return main_connection
