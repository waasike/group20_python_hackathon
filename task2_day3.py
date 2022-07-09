# CHALLENGE TASK TWO (Day 3)
number_of_fat_grams = int(input("Enter the number of fat grams consumed"))
number_of_carb_grams = int(input("Enter the number of carbohydrate grams consumed"))

calories_from_fat = number_of_fat_grams * 9
print("The calories from fat are", calories_from_fat)
calories_from_carbs = number_of_carb_grams * 4
print("The calories from carbohydrates are", calories_from_carbs)
total_calories = calories_from_fat * calories_from_carbs
print("You consumed", total_calories, "calories")