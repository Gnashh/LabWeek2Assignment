import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

def power(x, y):
    return x ** y

def square_root(x):
    if x < 0:
        return "Cannot calculate the square root of a negative number"
    return math.sqrt(x)

# Loop
while True:
    print("\n\n------------------------------------Welcome to Basic Math Calculator------------------------------------\n\n")
    print("Options:")
    print("Enter 'add' for addition")
    print("Enter 'subtract' for subtraction")
    print("Enter 'multiply' for multiplication")
    print("Enter 'divide' for division")
    print("Enter 'power' for division")
    print("Enter 'root' for square root")
    print("Enter 'quit' to stop")
    
    order = input("\nPlease choose from the option above: ")
    
    if order == "quit":
        break
    elif order in ["add", "subtract", "multiply", "divide"]:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if order == "add":
            print("Result:", add(num1, num2))
        elif order == "subtract":
            print("Result:", subtract(num1, num2))
        elif order == "multiply":
            print("Result:", multiply(num1, num2))
        elif order == "divide":
            print("Result:", divide(num1, num2))
    elif order == "power":
        num1 =  float(input("Enter the base number: "))
        num2 = float(input("Enter the exponent: "))
        print("Result:", power(num1, num2))
    elif order == "root":
        num = float(input("Enter a number: "))
        print("Result:", square_root(num))

    else:
        print("Invalid input. Please enter a valid operation.")
