import sqlalchemy
from connection import create_connection
from goodRoutes import good_id_by_name, menu_items


def main():
    conn = create_connection()

    sql = """ desc users """
    result = conn.execute(sqlalchemy.text(sql))

    for row in result:
        print(row)


if __name__ == '__main__':
    main()