
# Enter your choice from 1 to 5: 3
# Enter first number: 3
# Enter second number: 4

# 3.0 X 4.0 = 12.0

# Welcome to the Simple Calculator
# Select operation:
# 1. Addition
# 2. Subtraction
# 3. Multiplication
# 4. Division
# 5. Exit
# Enter your choice from 1 to 5: 5


def addition(first_num, second_num):
    return f"{first_num} + {second_num} = {first_num + second_num}"

def subtraction(first_num, second_num):
    return (first_num - second_num)

def multiplication(first_num,  second_num):
    return (first_num * second_num)

def division(first_num, second_num):
    if second_num == 0:
        return "Retry... Can't divide by zero"

    return f"{first_num} / {second_num} = {round(first_num / second_num), 2}"

while True:

    print('''
        ---- Welcome to the Simple Calculator----

        Select operation:

        1. Addition
        2. Subtraction
        3. Multiplication
        4. Division
        5. Exit
        
        ''')

    user_choice = input("Select an Operation from 1 - 5: ")

    if user_choice == "5":
        print("Exiting Calculator......")
        break

    if user_choice == "1":

        first_num =  float(input("Enter first number: "))
        second_num =  float(input("Enter second number: "))
        print(addition(first_num, second_num))

    elif user_choice == "2":
        first_num =  float(input("Enter first number: "))
        second_num =  float(input("Enter second number: "))
        print(f"{first_num} - {second_num} = {subtraction(first_num, second_num)}")

    elif user_choice == "3":
        first_num =  float(input("Enter first number: "))
        second_num =  float(input("Enter second number: "))
        print(f"{first_num} * {second_num} = {multiplication(first_num, second_num)}")

    elif user_choice == "4":
        first_num =  float(input("Enter first number: "))
        second_num =  float(input("Enter second number: "))

        print(division(first_num, second_num))
        

    else:
        print("Only choose an operation from 1 to 5")


