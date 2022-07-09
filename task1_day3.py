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
