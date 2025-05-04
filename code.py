print("Welcome to Tane's School Holiday Campo Registration")

camper_name = input("What is your name?")

while True: 
    camper_age= input("What is your age?")
    if camper_age.isdigit():
        age = int(camper_age)
        if 5<= age<=17:
            break
        else:
            print("Sory, the camp is only for children aged 5 to 17")
    else:
        print("Invalid input. Please enter a number for age")