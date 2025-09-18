def add( a, b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b
def divide(a,b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def calculator ():
    while True:
        print("Simple Calculator")
        print("Select operation:")
        print("1.Add")
        print("2.Subtract")
        print("3.Multiply")
        print("4.Divide")
        print("5.Exit")
        choice = input("Enter choice(1/2/3/4/5): ")
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

    
        if choice == '5':
            print("Exiting the calculator. Goodbye!")
            break

        if choice in ['1', '2', '3', '4']:

            match choice:
                case '1':
                    result = add(num1, num2)
                    print(f"{num1} + {num2} = {result}")
                case '2':
                    result = subtract(num1, num2)
                    print(f"{num1} - {num2} = {result}")
                case '3':
                    result = multiply(num1, num2)
                    print(f"{num1} * {num2} = {result}")
                case '4':
                    try:
                        result = divide(num1, num2)
                        print(f"{num1} / {num2} = {result}")
                    except ValueError as e:
                        print(e)
                case _:
                    print("Invalid input")

if __name__ == "__main__":
    calculator()