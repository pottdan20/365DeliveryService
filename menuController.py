import sqlalchemy
from connection import get_connection


def getMenuItems():
    conn = get_connection()
    sql = "SELECT Name, Cost FROM goods"

    result = conn.execute(sqlalchemy.text(sql))

    menu = []

    for row in result:
        menu.append(row)

    return menu


def getItemIdByName(item):
    conn = get_connection()
    result = conn.execute(sqlalchemy.text("SELECT gid FROM goods WHERE Name = :i"), [{"i": item}]).scalar()
    
    return result



