"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import * 


def calculator_2():

    while True:

        input_string = input("enter something ")
        tokens = input_string.split(" ")
        answer = None

        if len(tokens) < 3 and len(tokens) > 1:
            num1 = int(tokens[1])
        elif len(tokens) == 3:
            num1 = int(tokens[1])
            num2 = int(tokens[2])


        if input_string == "q":
            break

        elif tokens[0] == "-":
            answer = subtract(num1, num2)

        elif tokens[0] == "+":
            answer = add(num1, num2)

        elif tokens[0] == "*":
            answer = multiply(num1, num2)

        elif tokens[0] == "/":
            answer = divide(num1, num2)

        elif tokens[0] == "square":
            answer = square(num1)

        elif tokens[0] == "cube":
            answer = cube(num1)

        elif tokens[0] == "power":
            answer = power(num1, num2)

        elif tokens[0] == "mod":
            answer = mod(num1, num2)

        print(answer)

calculator_2()