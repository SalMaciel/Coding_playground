# Import random library
import random

def game ():
    # Title
    print("'Let's play rock paper scissors!")

    # Options
    options = ["r", "p", "s"]

    # Computer selection
    comp_choice = random.choice(options)

    # User selection
    user_choice = input("Make your choice: (r)ock, (p)aper, (s)cissors!: ")

    # Game logic
    if comp_choice == user_choice:
        print("It's a tie!")

    elif (comp_choice == "r" and user_choice == "p") \
        or (comp_choice == "p" and user_choice == "s") \
        or (comp_choice == "s" and user_choice == "r"):
        print("You win!")
    
    else:
        print("You Lose!")

again = "y"

while again == "y":
    game()
    again = input("Do you want to play again? (y)es, (n)o ")

exit()