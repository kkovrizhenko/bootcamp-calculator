# This is a “Console calculator" for a Python AQA Bootcamp task
import sys
from typing import Callable

valid_operators = ['+', '-', '/', '*']


def greet_at_start() -> None:
    """Greet person at the star of the program."""
    print("Welcome to the fancy console calculator!")


def instruction() -> None:
    """Provide user with instruction on how to use the program."""
    print("Please follow the guide below to face the magic of math."
          "\n Notes:"
          "\n - Click Enter after each step "
          "\n - Available math operators are: +, -, * and / "
          "\n - Type 'exit' at any step if you want to exit the calculator"
          "\n - Number can be a float number (6.66)")


def validate_number(num: str) -> bool:
    """Validate value for being a number and print a massage if the validation failed."""
    try:
        float(num)
        return True
    except ValueError:
        print('Please enter valid number')
        return False


def validate_operator(operator: str) -> bool:
    """Validate value for being in a list of operators and print a massage if the validation failed."""
    if operator in valid_operators:
        return True

    print(f'Please enter one on these operators: {", ".join(valid_operators)}')
    return False


def handle_input(phrase: str, validator: Callable[[str], bool]) -> T:
    """
    Wait for user's input, exit app or validate and return input

    :param phrase: guiding message for the user
    :param validator: function to validate user input
    :return: valid user input
    """
    res = input(phrase)

    if res == 'exit':
        app_exit()

    if not validator(res):
        res = handle_input(phrase, validator)

    return res


def read_user_inputs() -> None:
    """Ask user to enter 2 numbers and operators, process them and show result, rinse and repeat"""
    a = handle_input("Enter first number:", validate_number)
    operator = handle_input("Enter the operator you want to use:", validate_operator)
    b = handle_input("Enter second number:", validate_number)
    count(a, b, operator)
    read_user_inputs()


messages_dict = {
    '+': "The sum is: ",
    '-': "The result of negation is: ",
    '/': "The result of division: ",
    '*': "The result of multiplying: "
}

def count(a: str, b: str, operator: str) -> None:
    """
    Perform math operation based on user inputs and print result

    :param a: first number
    :param b: second number
    :param operator: math operator
    """
    calculation = f"{a}{operator}{b}"

    try:
        result = round(eval(calculation), 3)
        print(messages_dict[operator], result)
    except ZeroDivisionError:
        print("Hold you horses, you can't divide by 0! Try again!")
        read_user_inputs()


def app_exit() -> None:
    """Exit app"""
    sys.exit("Adios amigo!")


if __name__ == '__main__':
    greet_at_start()
    instruction()
    read_user_inputs()
