# This is a “Console calculator" for a Python AQA Bootcamp task
import sys

valid_operators = ['+', '-', '/', '*']


def greet_at_start():
    print("Welcome to the fancy console calculator!")


def instruction():
    print("Please follow the guide below to face the magic of math."
          "\n Notes:"
          "\n - Click Enter after each step "
          "\n - Available math operators are: +, -, * and / "
          "\n - Type 'exit' at any step if you want to exit the calculator"
          "\n - Number can be a float number (6.66)")


def validate_number(num):
    try:
        float(num)
        return True
    except ValueError:
        print('Please enter valid number')
        return False


def validate_operator(operator):
    if operator in valid_operators:
        return True

    print(f'Please enter one on these operators: {", ".join(valid_operators)}')
    return False


def handle_input(phrase, validator):
    res = input(phrase)

    if res == 'exit':
        app_exit()
        return

    if not validator(res):
        res = handle_input(phrase, validator)

    return res


def inputs():
    a = handle_input("Enter first number:", validate_number)
    operator = handle_input("Enter the operator you want to use:", validate_operator)
    b = handle_input("Enter second number:", validate_number)
    count(a, b, operator)


def count(a, b, operator):
    first_num = float(a)
    second_num = float(b)

    if operator == '+':
        print("The sum is :", round(first_num + second_num, 3))
    elif operator == '-':
        print("The result of negation is: ", round(first_num - second_num, 3))
    elif operator == '/':
        if second_num != float(0):
            print("The result of division: ", round(first_num / second_num, 3))
        else:
            print("Hold you horses, you can't divide by 0! Try again!")
            inputs()
    elif operator == '*':
        print("The result of multiplying: ", round(first_num * second_num, 3))


def app_exit():
    sys.exit("Adios amigo!")


def start() -> object:
    greet_at_start()
    instruction()
    inputs()

start()
