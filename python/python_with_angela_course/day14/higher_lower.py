from game_data import data
import random

logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

logo2 = vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""
print(logo)

def format(account):
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]

    return f"{account_name}, a {account_description}, from {account_country}"


def check_answer(user_guess, a_follow, b_follow):
    if b_follow > a_follow:
        return user_guess == "b"
    else:
        return user_guess == "a"

score = 0
should_continue = True

while should_continue == True:

    print(logo)

    account_a = random.choice(data)
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)


    print(f"Compare A: {format(account_a)}")
    print(logo2)
    print(f"Against B: {format(account_b)}")

    guess = input("Who has more followers? Type A or B:  ").lower()


    a_follower_account = account_a["follower_count"]
    b_follower_account = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_account, b_follower_account)


    if is_correct == True:
        score += 1
        import os
        clear = lambda:os.system('cls')
        clear()
        print(f"You got it right! Score: {score}.")
    else:
        print(f"Sorry, that's wrong. Your final score is {score}.")
        should_continue = False