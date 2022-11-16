import sqlalchemy
from connection import get_connection


def good_id_by_name(item):
    conn = get_connection()
    sql = sqlalchemy.text("SELECT gid FROM goods WHERE Name = :i").bindparams(i = item)

    try:
        result = conn.execute((sql)).first()[0]
    except:
        return None

    return result




def menu_items():
    conn = get_connection()
    sql = "SELECT Name, Cost FROM goods"

    result = conn.execute(sqlalchemy.text(sql))

    menu = []

    for row in result:
        menu.append(row)

    return menu


