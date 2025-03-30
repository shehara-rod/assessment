# this program is about asking a user to enter information on attending a school ball
print("Time for the school ball")
goingto_ball = input("Are you planning to go to the school ball? Type your answer as y or yes  ")
# the IF statement will check if the user's answers are yes to the question prompt
if goingto_ball.lower() == "y" or goingto_ball.lower() == "yes":
    taking_partner = input ("Are you planning to bring an out of school partner?  ")
    if taking_partner.lower() =="y" or taking_partner.lower() == "yes":
        print("Make sure you fill in the out of school partner form!")
    else:
        print("Make sure you fill in the permission slip")
else:
    print("You can still watch the students entering the hall at 8pm")