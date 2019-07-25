sales = float(input("Enter sales: $"))

while sales >= 0:
    if sales < 1000:
        bonus= sales*0.1
        print("Your bonus is $" + str(bonus))
    elif sales>=1000:
        bonus = sales * 0.15
        print("Your bonus is $" + str(bonus))

    sales = float(input("Enter sales: $"))
print("INVALID INPUT")

