import sqlalchemy
from connection import get_connection


def showTables():
    conn = get_connection()
    sql = "show tables"

    result = conn.execute(sqlalchemy.text(sql))

    for row in result:
        print(row)

def descItems():
    conn = get_connection()
    sql = "describe deliveryItems"

    result = conn.execute(sqlalchemy.text(sql))

    for row in result:
        print(row)

def selectAllUsers():
    conn = get_connection()
    sql = "select * from users"

    result = conn.execute(sqlalchemy.text(sql))

    for row in result:
        print(row)

def selectAllDeliveries():
    conn = get_connection()
    sql = "select * from deliveries"
    #sql = "delete from  deliveries where status=\'warehouse 1\'"
    result = conn.execute(sqlalchemy.text(sql))

    for row in result:
        print(row)

def selectAllDeliveryItems():
    conn = get_connection()
    sql = "select * from deliveryItems"
    result = conn.execute(sqlalchemy.text(sql))

    for row in result:
        print(row)

def describeDeliveries():
    conn = get_connection()
    sql = "describe deliveries"

    result = conn.execute(sqlalchemy.text(sql))

    for row in result:
        print(row)


if __name__ == '__main__':
    selectAllDeliveryItems()