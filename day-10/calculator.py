from re import I, sub


def sum(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": sum,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    num1 = float(input("What's the first number? "))
    for operation in operations:
        print(operation)

    should_continue = True
    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("Whats the next number? "))
        answer = operations[operation_symbol](num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer} ")

        if input("Press 'y' to continue or 'n' to start a new calculation ") == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator() #recursion

calculator()