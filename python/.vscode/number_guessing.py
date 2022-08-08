user_input = input("Please enter your guess: ")
x = 23
counter = 0

while(counter <= 6):
    if int(user_input) == x:
        print("Congratulations! You guessed the number!")
        break
    else:
        print("try again!")
        counter = counter + 1
        user_input = input("Please enter your guess: ")

if counter > 6:
    print("Better luck next time! You lost!")
    print("The answer was " + str(x) + "!")
