import random

print("You can choose one of these:")
print("rock ✊")
print("paper 🧾")
print("scissors ✂️")
print("Game Starts Now!!!")

choices = ["rock", "paper", "scissors"]

user = input("Enter your choice: ").lower().strip()

if user not in choices:
    print("Invalid Choice! Please enter rock, paper, or scissors.")
else:
    ch = random.choice(choices)

    print("Computer chose:", ch)

    if user == ch:
        print("Match Draw!!!")

    elif user == "rock" and ch == "paper":
        print("Computer Wins")

    elif user == "paper" and ch == "rock":
        print("You Win 🎉")

    elif user == "rock" and ch == "scissors":
        print("You Win 🎉")

    elif user == "scissors" and ch == "rock":
        print("Computer Wins 🎉")

    elif user == "paper" and ch == "scissors":
        print("Computer Wins 🎉")

    elif user == "scissors" and ch == "paper":
        print("You Win 🎉")
        