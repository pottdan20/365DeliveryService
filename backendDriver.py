import sqlalchemy
from connection import create_connection, get_connection
from goodRoutes import good_id_by_name, menu_items
from userController import createUser, attemptLogin
from driverController import pickupDelivery, validPickupDelivery


def main():
    # conn = get_connection()

    # sql = """ SELECT * from users """
    # result = conn.execute(sqlalchemy.text(sql))

    # for row in result:
    #     print(row)

    # print(attemptLogin("b", "a"))
    result = validPickupDelivery(5)
    print(result)


if __name__ == '__main__':
    main()