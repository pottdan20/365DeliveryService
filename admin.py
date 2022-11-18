from adminController import getAvgRating, getAllAvgRatings, getMostPopularItems

arg = input("[1]: rating by id\n [2]: rating of all drivers\n[3]:most popular items")
if arg == "1":
    id = input("driverId: ")
    try:
        print("user id: " + str(id) + " avg rating: " + str(getAvgRating(id)))
    except:
        print("error")
elif arg == "2":
    try:
        for user in (getAllAvgRatings()):
            print(user[0] + ": " + str(user[1]))
    except:
        print("error")
elif arg == "3":
    count = input("number to display: ")
    try:
        for item in getMostPopularItems(count):
            print(item[0]+ ": " + str(item[1]))
    except:
        print("error")
    
    print()

