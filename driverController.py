import sqlalchemy
from connection import get_connection


def getAllAvailableDeliveries():
    conn = get_connection()
    sql = sqlalchemy.text("SELECT * FROM deliveries WHERE Status = \"Placed\"")
    # sql = sqlalchemy.text("SELECT * FROM deliveries WHERE DriverId = :i").bindparams(i=None)

    result = conn.execute(sql)

    # for row in result:
    #     print(row)

    return result


def checkIfDeliveryExist(DId):
    conn = get_connection()
    sql = sqlalchemy.text("SELECT COUNT(*) FROM deliveries WHERE DId = :e").bindparams(e = DId)
    result = conn.execute(sql).first()[0]
    if(result):
        return True
    return False

def pickupDelivery(UId, DId):
    conn = get_connection()
    sql = sqlalchemy.text("SELECT * FROM deliveries WHERE DId = :i").bindparams(i=DId)

    result = conn.execute(sql).first()

    return result