from adminController import getAvgRating, getAllAvgRatings, getMostPopularItems, getTotalDeliveries, getAvgDeliveryTimes

commands = [
    "[1]: Rating by id",
    "[2]: Ratings of all drivers",
    "[3]: Most popular items",
    "[4]: Number of deliveries per driver",
    "[5]: Avg of delivery time of all drivers",
    "[q]: Quit"
]
print()

print("Commands")
for command in commands:
    print(command)
print()

arg = ''

while arg != "q":
    arg = input("[1, 2, 3, 4, 5, q]: ")
    if arg == "1":
        id = input("DriverId: ")
        try:
            print("User Id: " + str(id) + " Avg rating: " + str(getAvgRating(id)))
        except:
            print("error")
        print()
    elif arg == "2":
        try:
            for user in (getAllAvgRatings()):
                print(user[0] + ": " + str(user[1]))
        except:
            print("error")
        print()
    elif arg == "3":
        count = input("Number of items to display: ")
        try:
            for item in getMostPopularItems(count):
                print(item[0]+ ": " + str(item[1]))
        except:
            print("error")
        print()
    elif arg == "4":
        try:
            for driver in (getTotalDeliveries()):
                print(driver[0] + ": " + str(driver[1]))
        except:
            print("error")
        print()
    elif arg == "5":
        try:
            for driver in (getAvgDeliveryTimes()):
                print(driver[0] + ": " + str(driver[1]))
        except:
            print("error")
        print()

