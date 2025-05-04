min_age = 5
max_age = 17



print("Welcome to Tane's School Holiday Campo Registration")

camp_names = ["Cultural Immersion", "kayaking and Pancakes", "Mountain Biking"]
camp_days = [5,3,4]
camp_difficulty = ["Easy","Moderate", "Difficult"]
camp_cost = [800,400,900]

camper_name = input("What is your name?   ")

while True: 
    camper_age= input("What is your age?   ")
    if camper_age.isdigit():
        age = int(camper_age)
        if min_age<= age<=max_age:
            break
        else:
            print(f"Sory, the camp is only for children aged {min_age} to {max_age}")
    else:
        print("Invalid input. Please enter a number for age")

print ("\nPlease choose a camp by entering a number:  ")

for i in range(len(camp_names)):
    print(f"{i + 1}. {camp_names[i]} ({camp_days[i]}days, {camp_difficulty[i]}, ${camp_cost[i]})")

camp_choice = input("Enter your camp choice (1 ,2, or 3) :  ")