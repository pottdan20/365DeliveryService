import sqlalchemy
import time    
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

def validPickupDelivery(DId):

    conn = get_connection()
    sql = sqlalchemy.text("SELECT * FROM deliveries WHERE DId = :e AND Status = \"Placed\"").bindparams(e = DId)
    result = conn.execute(sql).first()
    if(result):
        return True

    return False

def pickupDelivery(UId, DId):
    # Update delivery DriverId as UId
    # Update PickupTime to current time 
    # Change Status to "En Route"
    conn = get_connection()

    sql = sqlalchemy.text("UPDATE deliveries SET Status = \"En Route\", DriverId = :UId, PickupTime = NOW() WHERE DId = :DId AND Status = \"Placed\"").bindparams(UId=UId,DId=DId)

    with conn.begin():
        result = conn.execute(sql)

    return result

def completeDelivery(DId):    
    # update delivery Status to "Completed"
    # update DropoffTime to current time
    conn = get_connection()

    sql = sqlalchemy.text("UPDATE deliveries SET Status = \"Completed\", DropoffTime = NOW() WHERE DId = :DId AND Status = \"En Route\"").bindparams(DId=DId)

    with conn.begin():
        result = conn.execute(sql)

    return result   