from connection import get_connection
import sqlalchemy
def createDelivery(customerId, address, cart): #return order id
    conn = get_connection()
    sql = sqlalchemy.text("insert into deliveries (customerid,status,pickuplocation, droplocation) values (:id, \'placed\', \'warehouse 1\' , :d)").bindparams(id = customerId, d = address)
    result = conn.execute(sql)
    Did = result.lastrowid
    for item in cart:
        sql = sqlalchemy.text("insert into deliveryItems (DId, GId, Quantity) values (:d, :g, :q)").bindparams(d=Did, g=item.get("id"), q = item.get("count"))
        conn.execute(sql)
    return Did
def attemptToCancel(orderID):
    print("canceling 123333")

def canRate(id): #true if driver has not picked up order yet
    return True

def rateDelivery(id, rate):
    print("rating del")

if __name__ == '__main__':
    createDelivery([{}])
    