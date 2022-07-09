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