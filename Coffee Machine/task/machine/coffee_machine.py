print("Write how much cups of coffee you will need.")
num_cups = int(input())
water = str(num_cups * 200)
milk = str(num_cups * 50)
beans = str(num_cups * 15)
num_cups = str(num_cups)
print("For " + num_cups + " of coffee you will need:")
print(water + " ml of water")
print(milk + " ml of milk")
print(beans + " g of coffee beans")
