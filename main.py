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
        total_price_of_paint = number_of_gallons * price_gallon
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




# DOOR LOCK SYSTEM CHALLENGE – Task One (Day 3)





# CHALLENGE TASK TWO (Day 3)
number_of_fat_grams = int(input("Enter the number of fat grams consumed"))
number_of_carb_grams = int(input("Enter the number of carbohydrate grams consumed"))

calories_from_fat = number_of_fat_grams * 9
print("The calories from fat are", calories_from_fat)
calories_from_carbs = number_of_carb_grams * 4
print("The calories from carbohydrates are", calories_from_carbs)
total_calories = calories_from_fat * calories_from_carbs
print("You consumed", total_calories, "calories")