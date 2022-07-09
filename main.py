# THIS IS ALL THE PROJECT CODE COMBINED
# BUS FARE CHALLENGE - Task One (Day 1)
import datetime 

date = datetime.datetime.now()
day = date.strftime("%A")[0:3]
weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri"]

print("Date :", date)
print("Day:", day)

if day in weekdays:
    print("Fare:", 100)
elif day == "Sat":
    print("Fare:", 60)
elif day == "Sun":
    print("Fare:", 80)

# SALES TAX CHALLENGE - Task Two (Day 1)
def main():
    square_footage = input("Enter the number of square feet to be painted")
    price_gallon = input("Enter the price of the paint per gallon")

    estimate(square_footage, price_gallon)

    def estimate(square_footage, price_gallon):

        num_gallons = square_footage / 115
        hours_of_labor = num_gallons * 8
        total_price_of_paint = num_gallons * price_gallon
        total_labor_charges = hours_of_labor * 20
        total_cost_of_job = total_price_of_paint + total_labor_charges
        print('The total estimated price for the paint job is $', total_cost_of_job)

main()   

# PERSONALITY TEST PROGRAM - Task One (Day 2)
number_of_books_purchased = int(input("Enter the number of books purchased this month"))

if number_of_books_purchased == 0:
    print(0, "points ")
elif number_of_books_purchased == 1:
    print(6, "points ")
elif number_of_books_purchased == 2:
    print(16, "points")
elif number_of_books_purchased == 3:
    print(32, "points")
elif number_of_books_purchased == 4:
    print(60, "points")

# CHALLENGE - Task Two (Day 2)
# This question was quite vage for us to understand but we just used some of the knowledge we had in python to hack it !
print("Q1.Which career deals with study of computers and computing as well as their theoretical and practical applications? \n")
print("Q2.Which career deals with developing strategies for analyzing data, preparing data for analysis \n")
print("Q3.Which career deals with application of principles used in the field of engineering and management of software systems \n")
print("Q4.Which career deals with developing a website for the Internet \n")
print("Q5.Which career deals with set of technologies that protects the usability and integrity of a company's infrastructure ")

user_input = input("Enter your career question number based on the questions above")

option1 = "Computer Science"
option2 = "Data Science"
option3 = "Software Engineering"
option4 = "Web Development"
option5 = "Network Security"

carrier_advices = [
    "Pick a career based on your interests"
    "Pick a career based on your ability"
    "Pick a career based on set financial goals (salary)"
]
carrier_questions = [
    "Which career deals with study of computers and computing as well as their theoretical and practical applications? \n"
    "Which career deals with developing strategies for analyzing data, preparing data for analysis \n"
    "Which career deals with application of principles used in the field of engineering and management of software systems \n"
    "Which career deals with developing a website for the Internet \n"
    "Which career deals with set of technologies that protects the usability and integrity of a company's infrastructure " 
]

if user_input == "Q1":
    print("Your career is: ", option1)
elif user_input == "Q2":
    print("Your career is: ", option2)
elif user_input == "Q3":
    print("Your career is: ", option3)
elif user_input == "Q4":
    print("Your career is: ", option4)
elif user_input == "Q5":
    print("Your career is: ", option5)


# DOOR LOCK SYSTEM CHALLENGE – Task One (Day 3)
import datetime 
Previous_Date = datetime.datetime.today() - datetime.timedelta()
password = "password"
open = "open"
close = "close"
quit = "quit"
user_input = input("Enter password: ")

while user_input != password:
  print("Error!, Enter your password again")
  user_input = input("Enter password: ")
else:
    print("Correct password, You have succesfully gotten access to the door")
    user_command = input("Enter a command for the door")
    if user_command == open:
        print("The door is now open")
        print("Door last open at: ", Previous_Date)
    elif user_command == close:
        print("The door is now locked")
        print("Door last looked at: ", Previous_Date)
    elif user_command == quit:
        print("The process has been terminated")
    elif user_command != open or user_command != close or user_command!= quit:
           print("Invalid input")
    
    user_command2 = input("Enter another command for the door")
    if user_command2 == open:
        if user_command == user_command2:
            print("The door is already open")
        else:    
            print("The door is now open")
            print("Door last open at: ", Previous_Date)
    elif user_command2 == close:
        if user_command == user_command2:
            print("The door is alrerady locked")
        else:
            print("The door is looked")
            print("Door last looked at: ", Previous_Date)
    elif user_command2 == quit:
        print("The process has been terminated")
       
    elif user_command2 != open or user_command2 != close or user_command2 != quit:
            print("Invalid input")

# CHALLENGE TASK TWO (Day 3)
number_of_fat_grams = int(input("Enter the number of fat grams consumed"))
number_of_carb_grams = int(input("Enter the number of carbohydrate grams consumed"))

calories_from_fat = number_of_fat_grams * 9
print("The calories from fat are", calories_from_fat)
calories_from_carbs = number_of_carb_grams * 4
print("The calories from carbohydrates are", calories_from_carbs)
total_calories = calories_from_fat * calories_from_carbs
print("You consumed", total_calories, "calories")