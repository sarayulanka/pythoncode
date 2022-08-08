logo = '''╔═══╗                     ╔╗ ╔╗                      ╔╗         
║╔═╗║                    ╔╝╚╗║║                      ║║         
║║ ╚╝╔╗╔╗╔══╗╔══╗╔══╗    ╚╗╔╝║╚═╗╔══╗    ╔═╗ ╔╗╔╗╔╗╔╗║╚═╗╔══╗╔═╗
║║╔═╗║║║║║╔╗║║══╣║══╣     ║║ ║╔╗║║╔╗║    ║╔╗╗║║║║║╚╝║║╔╗║║╔╗║║╔╝
║╚╩═║║╚╝║║║═╣╠══║╠══║     ║╚╗║║║║║║═╣    ║║║║║╚╝║║║║║║╚╝║║║═╣║║ 
╚═══╝╚══╝╚══╝╚══╝╚══╝     ╚═╝╚╝╚╝╚══╝    ╚╝╚╝╚══╝╚╩╩╝╚══╝╚══╝╚╝ 
                                                                
'''
import random

print(logo)
print("Welcome to the guess my number game!")
print("I am thinking of a number from 1 to 100.")

mystery_number = random.choice(range(1, 101))
print(f"Psst! The number is {mystery_number}!")

difficulty_level = input("Choose a difficulty level: easy or hard:  ").lower()


def easy_level():
    counter = 10
    print("You have 10 attempts.")
    user_guess = input("Please enter a guess:  ")
    counter -= 1
    print(f" You have {counter} attempts left.")
    while counter >= 0:
        if int(user_guess) == mystery_number:
            print("You guessed the mystery number! Great job!")
            break
        else:
            if int(user_guess) > mystery_number:
                print("Too high.")
                user_guess = input("Please enter a guess:  ")
                counter -= 1
                print(f" You have {counter} attempts left.")
            else:
                print("Too low.")
                user_guess = input("Please enter a guess:  ")
                counter -= 1
                print(f" You have {counter} attempts left.")
    
    
    if int(user_guess) != mystery_number and counter < 0:
        print("You couldn't guess the number. You lost.")


def hard_level():
    counter = 5
    print("You have 5 attempts.")
    user_guess = input("Please enter a guess:  ")
    counter -= 1
    print(f" You have {counter} attempts left.")
    while counter >= 0:
        if int(user_guess) == mystery_number:
            print("You guessed the mystery number! Great job!")
            break
        else:
            if int(user_guess) > mystery_number:
                print("Too high.")
                user_guess = input("Please enter a guess:  ")
                counter -= 1
                print(f" You have {counter} attempts left.")
            else:
                print("Too low.")
                user_guess = input("Please enter a guess:  ")
                counter -= 1
                print(f" You have {counter} attempts left.")
    
    
    if int(user_guess) != mystery_number and counter < 0:
        print("You couldn't guess the number. You lost.")

if difficulty_level == "easy":
    easy_level()
else:
    hard_level()