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
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("❌ Invalid input. Please enter numbers only.")
        continue

    match choice:
        case '1':
            print("✅ Result:", add(num1, num2))
        case '2':
            print("✅ Result:", subtract(num1, num2))
        case '3':
            print("✅ Result:", multiply(num1, num2))
        case '4':
            print("✅ Result:", divide(num1, num2))
