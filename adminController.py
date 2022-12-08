import sqlalchemy
import time    
from connection import get_connection

def getAvgRating(DriverId):  # returns average driver rating
    conn = get_connection()

    result = conn.execute(sqlalchemy.text("SELECT AVG(Rating) FROM deliveries WHERE Driverid = :id AND Status = 'Dropped' AND rating IS NOT NULL"),
         [{"id": DriverId}]).scalar()

    return result 

def getAllAvgRatings():  # returns list of [(name, avg driver rating), ...]
    conn = get_connection()
    sql = sqlalchemy.text("""select * from (SELECT FirstName, LastName, AVG(Rating) r
      FROM deliveries 
      JOIN users on users.UId = deliveries.DriverId
      WHERE Status = "dropped" AND Rating IS NOT NULL 
      GROUP BY FirstName, LastName) as t order by r desc""" )

    result = conn.execute(sql)

    ratings = []

    for row in result:
      ratings.append((row[0] + " " + row[1], row[2]))

    return ratings 

def getMostPopularItems(rank):
    conn = get_connection()

    result = conn.execute(sqlalchemy.text("""
      WITH rankedGoods as (SELECT Name, COUNT(*) Total, RANK() OVER (ORDER BY COUNT(*) DESC) ranking
      FROM deliveryItems
      JOIN goods on goods.GId = deliveryItems.GId
      GROUP BY Name
      ORDER BY ranking ASC, Name ASC)

      SELECT Name, Total FROM rankedGoods
      WHERE ranking <= :r """),[{"r": rank}])

    items = []

    for row in result:
      items.append((row[0], row[1]))

    return items


#  !!! NOT COMPLETE !!!
# Need to validate Month and Year before running this function
def getMonthlySpending(UId, month, year):  # returns sum cost of goods purchased by user in specified month
  conn = get_connection()

  result = conn.execute(sqlalchemy.text(""" 
  SELECT SUM(Cost)
  FROM deliveryItems
  JOIN goods on goods.GId = deliveryItems.GId
  JOIN deliveries on deliveries.DId = deliveryItems.DId
  WHERE CustomerId = :UId
  AND MONTH(PlacedTime) = :m
  AND YEAR(PlacedTime) = :y
  """),[{"UId": UId, "m": month, "y": year}]).scalar()

  return result

def getTotalDeliveries():
  conn = get_connection()
  result = conn.execute(sqlalchemy.text("""
  SELECT 
    CONCAT(FirstName, " ", LastName) as Driver,
    Count(*) TotalDeliveries
  FROM deliveries 
  JOIN users on users.UId = deliveries.DriverId
  WHERE Status = "dropped" or Status = "Dropped"
  GROUP BY Driver
  ORDER BY TotalDeliveries DESC
  """))

  drivers = []

  for row in result:
    drivers.append((row[0], row[1]))

  return drivers

def getAvgDeliveryTimes():
  conn = get_connection()
  result = conn.execute(sqlalchemy.text("""
  WITH difference_in_seconds AS (
    SELECT 
        CONCAT(FirstName, " ", LastName) as Driver,
        AVG(TIMESTAMPDIFF(SECOND, PickupTime, DropoffTime)) as seconds
    FROM deliveries 
    JOIN users on users.UId = deliveries.DriverId
    WHERE Status = "dropped" or Status = "Dropped"
    GROUP BY Driver
    ORDER BY seconds ASC
  )

  SELECT
    Driver,
    CONCAT(
      FLOOR(seconds / 60), ' minutes ',
      ROUND(MOD(seconds, 60), 0), ' seconds'
    ) AS AvgDeliveryTime
  FROM difference_in_seconds
  """))

  drivers = []

  for row in result:
    drivers.append((row[0], row[1]))

  return drivers

