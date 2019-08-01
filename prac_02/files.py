names=open('name.txt', 'w')
print("Your name is Bob.", file=names)

names.close()

numbers = open("numbers.txt", "r")
num1=numbers.readline()
num2=numbers.readline()
result = int(num1) +int(num2)
print(result)

manyNumbers= open("manyNumbers.txt", "r")

total= 0
for i in manyNumbers:
    total = total + int(i)
print(total)