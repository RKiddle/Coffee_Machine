# Checking amounts of ingredients
print("How much water is available?")
water_now = int(input())
# Checking amounts of ingredients
water_now = int(input())
milk_now = int(input())
coffee_now = int(input())
# Number of ordered cups of coffee
num_cups_needed = int(input())
# Calculation of number of cups that can be made
# Water_used = ratio of water
cups_made = min(water_now//200, milk_now//50, coffee_now//15)
extra_cups = cups_made - num_cups_needed
if cups_made == num_cups_needed:
    print("Yes, I can make that amount of coffee")
elif cups_made > num_cups_needed:
    print(f"Yes, I can make that amount of coffee (and even {extra_cups} more than that)")
elif cups_made < num_cups_needed:
    print(f"No, I can make only {cups_made} cups of coffee")


