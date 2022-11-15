import sqlalchemy
from connection import get_connection


def good_id_by_name(item):
    conn = get_connection()
    sql = "SELECT * FROM goods WHERE Name = \"%s\"" % item

    result = conn.execute(sqlalchemy.text(sql)).first()[0]

    return result

def menu_items():
    conn = get_connection()
    sql = "SELECT Name, Cost FROM goods"

    result = conn.execute(sqlalchemy.text(sql))

    menu = []

    for row in result:
        menu.append(row)

    return menu
