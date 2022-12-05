from connection import get_connection
import sqlalchemy
def createDelivery(customerId, address, cart): #return order id
    conn = get_connection()
    with conn.begin():
        sql = sqlalchemy.text("insert into deliveries (customerid,status,pickuplocation, droplocation) values (:id, \'Placed\', \'warehouse 1\' , :d)").bindparams(id = customerId, d = address)
        result = conn.execute(sql)
        Did = result.lastrowid
        for item in cart:
            sql = sqlalchemy.text("insert into deliveryItems (DId, GId, Quantity) values (:d, :g, :q)").bindparams(d=Did, g=item.get("id"), q = item.get("count"))
            conn.execute(sql)

    return Did
def attemptToCancel(orderID): #cancel order if its not delivered. return false if it has been delivered, true if not and canceled
    conn = get_connection()
    sql = sqlalchemy.text("select status from deliveries where did = :id").bindparams(id = orderID)
    result = conn.execute(sql)
    if result.first()[0] == "Completed":
        return False
    
    sql = sqlalchemy.text("update deliveries set status = \'Canceled\' where did = :id").bindparams(id = orderID)
    conn.execute(sql)
    return True

def canRate(id): #true if driver has not picked up order yet
    conn = get_connection()
    with conn.begin():
        sql = sqlalchemy.text(" Select status from deliveries where Did = :did").bindparams(did = id)
        result = conn.execute(sql).first()[0]
        if result != "Completed":
            return False
        return True

def rateDelivery(id, rate):
    conn = get_connection()
    sql = sqlalchemy.text(" update deliveries set rating = :r where Did = :did").bindparams(did = id, r=rate)
    result = conn.execute(sql)

def tipDelivery(id, tip):
    conn = get_connection()
    sql = sqlalchemy.text("update deliveries set tip = :t where Did = :did").bindparams(did = id, t=tip)
    result = conn.execute(sql)

def getTip(id):
    conn = get_connection()
    sql = sqlalchemy.text(" Select tip from deliveries where Did = :did").bindparams(did = id)
    result = conn.execute(sql)
    return result.first()[0]
    

if __name__ == '__main__':
    createDelivery([{}])
    