# calculator.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide (a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("You cannot divide by zero")


print("🧮 Welcome to CLI Calculator 🧮")

firstOp = False
calculatedValue = 0
while True:
    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter choice (1/2/3/4/5): ")

    if choice == '5':
        print("👋 Exiting calculator. Have a great day!")
        break

    try:
        if(firstOp == False):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        else:
            num1 = float(calculatedValue)
            num2 = float(input("Enter a number: "))

    except ValueError:
        print("❌ Invalid input. Please enter numbers only.")
        continue

    firstOp = True
    match choice:
        case '1':
            calculatedValue = add(num1, num2)
            print(num1, '+', num2, '=', calculatedValue)
        case '2':
            calculatedValue = subtract(num1, num2)
            print(num1, '-', num2, '=', calculatedValue)
        case '3':
            calculatedValue = multiply(num1, num2)
            print(num1, 'x', num2, '=', calculatedValue)
        case '4':
            calculatedValue = divide(num1, num2)
            print(num1, '/', num2, '=', calculatedValue)

