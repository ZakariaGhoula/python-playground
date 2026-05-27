

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a*b;

def divide (a, b):
    try:
        return a/b;
    except ZeroDivisionError:
        print("You cannot divide by zero")


final = 0
while True:
    print(final)
    number = input("Enter a number: ")
    operator = input("Enter a operator(+,-,x,*,/): ")
    match operator:
        case "+":
          final = add(final, int(number))
        case "-":
            final = subtract(final, int(number))
        case "X" | "*":
            final = multiply(final, int(number))
        case '/':
            final = divide(final, int(number))
