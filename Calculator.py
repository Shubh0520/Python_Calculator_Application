"""Function declaration for Addition Operation"""


def addition_operation(user_input_1, user_input_2):
    add_operation = (user_input_1 + user_input_2)
    return add_operation


"""Function declaration for Subtraction Operation"""


def subtraction_operation(user_input_1, user_input_2):
    sub_operation = (user_input_1 - user_input_2)
    return sub_operation


"""Function declaration for Multiplication Operation"""


def multiply_operation(user_input_1, user_input_2):
    multiply_operation = (user_input_1 * user_input_2)
    return multiply_operation


"""Function declaration for Division Operation"""


def division_operation(user_input_1, user_input_2):
    div_operation = (user_input_1 / user_input_2)
    return div_operation


# Taking input from the user for various operations

operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')
user_input_1 = float(input("Enter first Number: "))
user_input_2 = float(input("Enter second Number: "))

# Check if choice is one of the four options
if operation == '+':
    print(f"{user_input_1} + {user_input_2} = {addition_operation(user_input_1, user_input_2)}")

elif operation == '-':
    print(f"{user_input_1} - {user_input_2} = {subtraction_operation(user_input_1, user_input_2)}")

elif operation == '*':
    print(f"{user_input_1} * {user_input_2} = {multiply_operation(user_input_1, user_input_2)}")

elif operation == '/':
    print(f"{user_input_1} / {user_input_2} = {division_operation(user_input_1, user_input_2)}")

else:
    print("OOPS! You have given invalid Input")
