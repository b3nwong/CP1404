"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

finished = False
result = 0
while not finished:
    try:
        x= int(input("input a numerator: "))
        y=int(input("input a denominator: "))
        result=x/y
        break

    except ValueError:
        print("Please enter a valid integer.")
print("Valid result is:", result)