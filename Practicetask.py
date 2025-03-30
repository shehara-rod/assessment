name = input("Enter your name:  ")
age = int(input("Enter your age:  "))

activities = {
    "1" : ("Music Jam Sessions", 2, "easy", 5),
    "2" : ("Science Experiments Lab", 3,"moderate",10),
    "3" : ("Sports Leadership Training",4,"challenging",12)
}
print("\nChoose an activity")
print("1. Music Jam Session (2 hours, easy, $5 fee)")
print("2. Science Experiments Lab (3 hours, moderate, $10 fee)")
print("3. Sports Leadership Training (4 hours, challenging, $12 fee)")

activity_choice = input ("Enter the number of your chosen activity:  ")
