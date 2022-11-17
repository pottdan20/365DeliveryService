import sqlalchemy
from connection import get_connection
import hashlib
   
    # conn = get_connection()
    # sql = "SELECT * FROM goods WHERE Name = \"%s\"" % item

    # result = conn.execute(sqlalchemy.text(sql)).first()[0]

    # return result

def checkIfUserExist(email):
    conn = get_connection()
    sql = sqlalchemy.text("SELECT COUNT(*) FROM users WHERE email = :e").bindparams(e = email)
    result = conn.execute(sql).first()[0]
    if(result):
        return True
    return False

def createUser(email, password): # create and return the user object created
    hashedPass = hashlib.sha256(password.encode("utf-8")).hexdigest()
    print("creating " + email + "...")
    conn = get_connection()
    sql = sqlalchemy.text("insert into users (email,password) values (:e, :p)").bindparams(e = email, p = hashedPass)
    result = conn.execute(sql)
    return result.lastrowid
    
def checkRollback():
    password = "test"
    hashedPass = hashlib.sha256(password.encode("utf-8")).hexdigest()
    print("creating " + "...")
    conn = get_connection()
    sql = sqlalchemy.text("insert into users (email,password) values (:e, :p)").bindparams(e = "testRollback2", p = hashedPass)
    with conn.begin():
        result1 = conn.execute(sql)
        result2 = conn.execute(sqlalchemy.text("showTables"))


def deleteUser(email):
    conn = get_connection()
    sql = sqlalchemy.text("delete from users where email = :e").bindparams(e = email)
    result = conn.execute(sql)


def attemptLogin(email, password): #will attempt to login with current credentials and either throw an error if no user exisits
    conn = get_connection()
    sql = sqlalchemy.text("select uid from users where email = :e and password = :p").bindparams(e = email, p = hashlib.sha256(password.encode("utf-8")).hexdigest())
    
    result = conn.execute(sql).first()[0]          # or will return user object
    return result                        

if __name__ == '__main__':
    checkRollback()
