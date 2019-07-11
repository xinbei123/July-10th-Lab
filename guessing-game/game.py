
"""A number-guessing game."""

from random import randint

print("Howdy, what's your name?")

player_name = input("(type in your name) " )

start_num = int(input("Please pick a start number "))
end_num = int(input("Please pick a end number "))

random_number = randint(start_num,end_num)

print("{}, I'm thinking of a number between {} and {}. Try to guess my number.".format(player_name, start_num, end_num))

num_of_guess = 0
num_of_tries = []
difficuty = end_num - start_num
easy_point = 0
hard_point = 0

while True:
    try:
        guess_num = int(input("Your guess? "))
        num_of_guess += 1

        if num_of_guess > 8:
            print("Too many tries!")
            break

        elif guess_num < start_num or guess_num > end_num:
            print("This is not a valid number, please re-enter your number.")
        
        elif guess_num > random_number:
            print("Your guess is too high! Try again.")  

        elif guess_num < random_number:
            print("Your guess is too low! Try again.")

        else:
            print("Well done {}! You found my number in {} tries!".format(player_name, num_of_guess))

            if difficuty <= 10:
                easy_point += 1
                print("You earnd {} easy point.".format(easy_point))
                num_of_tries.append(num_of_guess)
                num_of_guess = 0
                print("Lowest number of guesses made: ", min(num_of_tries))
        
                random_number = randint(start_num,end_num)
                
        
    except ValueError:
        print("Invalid entry, please re-enter your number.")

       
            
