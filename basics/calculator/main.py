numbers = input("Give me n numbers: ").split()

for num in numbers:
    print("The number is:", num)


for i, v in enumerate(numbers):
    print("The number #",i+1, "is:", v)