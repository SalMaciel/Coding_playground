# Import random library
import random

# Title
print("'Let's play rock paper scissors!")

# Options
options = ["r", "p", "s"]

# Computer selection
comp_choice = random.choice(options)

# User selection
user_choice = input("Make your choice: (r)ock, (p)aper, (s)cissors!")

# Game logic

if comp_choice == user_choice:
    print("It's a tie!")
elif comp_choice == "r" and user_choice == "p":
    print("You win!")
elif comp_choice == "p" and user_choice == "s":
    print("You win!")
elif comp_choice == "s" and user_choice == "r":
    print("You win!")
else:
    print("You Lose!")