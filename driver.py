import sys
import sqlalchemy
import urllib.parse


def main():
    import os
    from dotenv import load_dotenv

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


# main(sys.argv)
if __name__ == '__main__':
    main()