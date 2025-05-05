min_age = 5
max_age = 17
shuttle_cost = 80



print("Welcome to Tane's School Holiday Campo Registration")

camp_names = ["Cultural Immersion", "kayaking and Pancakes", "Mountain Biking"]
camp_days = [5,3,4]
camp_difficulty = ["Easy","Moderate", "Difficult"]
camp_cost = [800,400,900]
meal_options = ["standard", "vegetarian", "vegan"]

camper_name = input("What is your name?   ")

while True: 
    camper_age= input("What is your age?   ")
    if camper_age.isdigit():
        age = int(camper_age)
        if min_age<= age<=max_age:
            break
        else:
            print(f"Sorry, the camp is only for children aged {min_age} to {max_age}")
    else:
        print("Invalid input. Please enter a number for age")

print ("\nPlease choose a camp by entering a number:  ")

for i in range(len(camp_names)):
    print(f"{i + 1}. {camp_names[i]} ({camp_days[i]}days, {camp_difficulty[i]}, ${camp_cost[i]})")

while True:
    camp_choice = input("Enter your camp choice (1 ,2, or 3) :  ")
    if camp_choice in ['1', '2','3']:
        index = int(camp_choice) - 1
        break
    else:
        print ("Invalid choice. Please enter either 1, 2 or 3")

chosen_camp = camp_names[index]
days = camp_days [index]
difficulty = camp_difficulty[index]
cost = camp_cost [index]


print("\nMeal options: Standard, Vegetarian, Vegan")
while True:
    meal = input("Enter your meal choice:  ")
    if meal in meal_options:
        break
    else:
        print("Invalid choice. Please choose from standard, vegetarian or vegan")

chosen_meal = meal_options[index]

while True:
    transport = input("Do you want to use the shuttle service for $80? (yes/no)").strip().lower()
    if transport in ['yes' or 'no']:
        break
    else:
        cost += cost

if transport == 'yes':
    cost += shuttle_cost

    

confirm = input("Do you want to confirm your registraion ? 'yes' or 'no'").strip().lower()

print(f"Name:    {camper_name}")
print(f"Age:  {camper_age}")
print(f"Chosen camp type:  {chosen_camp}")
print(f"Number of days: {days}")
print(f"Difficulty level: {difficulty}")
print(f"Meal_choice:  {chosen_meal}")

print (f"Total cost: ${cost}")
print (f"Confirmed: {'Yes' if confirm =='yes' else 'No'}")
