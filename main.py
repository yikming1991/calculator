def plus(n1, n2):
    return n1 + n2


def minus(n1, n2):
    return n1 - n2


def times(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {"+": plus,
              "-": minus,
              "*": times,
              "/": divide,
              }
calculator_run = True
num1 = float(input("What's the first number?: "))
while calculator_run:
    num2 = float(input("What's the next number?: "))
    for operator in operations:
        print(operator, end="  ")
    operator = input("\nPick an operation from the list above.: ")
    calculator_function = operations[operator]
    result = calculator_function(num1, num2)
    print(f"{num1} {operator} {num2} = {result}")
    to_continue = input(f"Type 'y to continue calculating with {result}, or type 'n' to end the calculation. ").lower()
    if to_continue == "y":
        num1 = result
    else:
        calculator_run = False
        print("Goodbye")
