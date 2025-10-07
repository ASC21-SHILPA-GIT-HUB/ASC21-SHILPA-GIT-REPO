def simple_calculator(a, b, operation):
    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
    elif operation == 'divide':
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operation"
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
operation=input("Enter operation (add, subtract, multiply, divide): ")
result=simple_calculator(a, b, operation)
print(f"The result of {operation}ing {a} and {b} is: {result}")