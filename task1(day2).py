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