import sqlalchemy
from connection import get_connection


def showTables():
    conn = get_connection()
    sql = "show tables"

    result = conn.execute(sqlalchemy.text(sql))

    for row in result:
        print(row)

def selectAllUsers():
    conn = get_connection()
    sql = "select * from users"

    result = conn.execute(sqlalchemy.text(sql))

    for row in result:
        print(row)

if __name__ == '__main__':
    selectAllUsers()