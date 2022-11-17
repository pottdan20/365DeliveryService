import sqlalchemy
import time    
from connection import get_connection

def getAvgRating(DriverId):  # returns average driver rating
    conn = get_connection()
    sql = sqlalchemy.text("SELECT AVG(Rating) FROM deliveries WHERE DriverId = :id AND Status = \"Completed\" AND Rating IS NOT NULL").bindparams(id=DriverId)

    result = conn.execute(sql).first()[0]

    return result 

def getAllAvgRatings():  # returns list of [(name, avg driver rating), ...]
    conn = get_connection()
    sql = sqlalchemy.text("""SELECT FirstName, LastName, AVG(Rating) 
      FROM deliveries 
      JOIN users on users.UId = deliveries.DriverId
      WHERE Status = "Completed" AND Rating IS NOT NULL 
      GROUP BY FirstName, LastName
      ORDER BY LastName ASC, FirstName ASC""" )

    result = conn.execute(sql)

    ratings = []

    for row in result:
      ratings.append((row[0] + " " + row[1], row[2]))

    return ratings 

def getMostPopularItems(rank):
    conn = get_connection()
    sql = sqlalchemy.text("""
      WITH rankedGoods as (SELECT Name, COUNT(*) Total, RANK() OVER (ORDER BY COUNT(*) DESC) ranking
      FROM deliveryItems
      JOIN goods on goods.GId = deliveryItems.GId
      GROUP BY Name
      ORDER BY ranking ASC, Name ASC)

      SELECT Name, Total FROM rankedGoods
      WHERE ranking <= :r """).bindparams(r=rank)

    result = conn.execute(sql)

    items = []

    for row in result:
      items.append((row[0], row[1]))

    return items


#  !!! NOT COMPLETE !!!
# Need to validate Month and Year before running this function
def getMonthlySpending(UId, month, year):  # returns sum cost of goods purchased by user in specified month
  conn = get_connection()
  sql = sqlalchemy.text(""" 
  SELECT SUM(Cost)
  FROM deliveryItems
  JOIN goods on goods.GId = deliveryItems.GId
  JOIN deliveries on deliveries.DId = deliveryItems.DId
  WHERE CustomerId = :UId
  AND MONTH(PlacedTime) = :m
  AND YEAR(PlacedTime) = :y
  """).bindparams(UId=UId,m=month,y=year)

  result = conn.execute(sql).first()[0]

  return result
