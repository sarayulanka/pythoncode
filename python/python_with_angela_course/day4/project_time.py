# Now, using our knowledge of randomization, lists, and other things we have learned in the past,
# we are going to create a rock paper scissors game!
# Let's start creating the program.

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random

user_choice = int(input("What do you choose? 0 for rock, 1 for paper, 2 for scissors.  "))
computer_choice = random.randint(0, 2)

if user_choice == 0:
    print("You chose: " + rock)
elif user_choice == 1:
    print(f"You chose: " + paper)
else:
    print("You chose: " + scissors)


if computer_choice == 0:
    print("Computer chose: " + rock)
elif computer_choice == 1:
    print(f"Computer chose: " + paper)
else:
    print("Computer chose: " + scissors)


if user_choice == 2 and computer_choice == 0:
    print("You lose.")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif user_choice == 1 and computer_choice == 0:
    print("You win!")
elif user_choice == 0 and computer_choice == 1:
    print("You lose.")
elif user_choice == computer_choice:
    print("It's a tie!")
elif user_choice == 1 and computer_choice == 2:
    print("You lose.")
elif user_choice == 2 and computer_choice == 1:
    print("You win!")