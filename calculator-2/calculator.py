"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import * 


# Your code goes here
while True:

    input_string = input("enter something ")
    tokens = input_string.split(" ")
    num1 = int(tokens[1])
    num2 = int(tokens[2])

    if input_string == "q":
        break

    elif tokens[0] == "-":
        answer = subtract(num1, num2)
        print(answer)

    elif tokens[0] == "+":
        answer = add(num1, num2)
        print(answer)

    elif tokens[0] == "*":
        answer = multiply(num1, num2)
        print(answer)

    elif tokens[0] == "/":
        answer = divide(num1, num2)
        print(answer)

    elif tokens[0] == "square":
        answer = square(num1, num2)
        print(answer)

    elif tokens[0] == "cube":
        answer = cube(num1, num2)
        print(answer)

    elif tokens[0] == "power":
        answer = power(num1, num2)
        print(answer)

    elif tokens[0] == "mod":
        answer = mod(num1, num2)
        print(answer)
