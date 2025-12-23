import random


def game():
    user_selection = input("Select the option from: Rock, Paper, Scissors : ")

    options = ["Rock", "Paper", "Scissors"]

    if user_selection.capitalize() not in options:
        print("Invalid selection")
        game()
    pc_selection = random.choice(options)
    print("PC choice: " + pc_selection)

    if user_selection.lower() == "rock" and pc_selection.lower() == "scissors":
        print("User win")
    elif user_selection.lower() == "scissors" and pc_selection.lower() == "rock":
        print("PC win")
    elif user_selection.lower() == "paper" and pc_selection.lower() == "rock":
        print("User win")
    elif user_selection.lower() == "rock" and pc_selection.lower() == "paper":
        print("PC win")
    elif user_selection.lower() == "scissors" and pc_selection.lower() == "paper":
        print("User win")
    elif user_selection.lower() == "paper" and pc_selection.lower() == "scissors":
        print("PC win")
    else:
        print("No winner")
    game()

game()