numItems = int(input("Please enter the number of items you have: "))
total = 0
for i in range (numItems):
    price = float(input("Please enter the price of the items: $"))
    while price <=0:
        print('INVALID input, please re-enter the price of said item.')
        price = float(input("Please enter the price of the items: $"))
    total= price+total

print("Your total for "+ str(numItems) + " items is ${:.2f}.".format(total))