import random

play = True
user_points = 0
computer_points = 0
tie_points = 0

choices = ["rock", "paper", "scissors"]

while play:
  while True:
    user_choice = input("Pick Rock, Paper or Scissors\nTo stop playing write quit: ").lower()

    if user_choice == "quit":
      print("Game Ended")
      print(f"Score:\nYou: {user_points}\nComputer: {computer_points}\nTies: {tie_points}")
      play = False
      break

    if user_choice != "rock" and user_choice != "paper" and user_choice != "scissors":
      print("Invalid choice")
    else:
      break

  computer_choice = random.choice(choices)

  if user_choice == computer_choice:
    print(f"You picked {user_choice.capitalize()} and the computer picked {computer_choice.capitalize()}")
    print("Is a tie")
    tie_points +=1
    print(f"Score:\nYou: {user_points}\nComputer: {computer_points}\nTies: {tie_points}")

  if user_choice == "rock":
    if computer_choice == "paper":
      print(f"You picked {user_choice.capitalize()} and the computer picked {computer_choice.capitalize()}")
      print("Computer Wins")
      computer_points += 1
      print(f"Score:\nYou: {user_points}\nComputer: {computer_points}\nTies: {tie_points}")
    elif computer_choice == "scissors":
      print(f"You picked {user_choice.capitalize()} and the computer picked {computer_choice.capitalize()}")
      print("You Win")
      user_points += 1
      print(f"Score:\nYou: {user_points}\nComputer: {computer_points}\nTies: {tie_points}")

  if user_choice == "paper":
    if computer_choice == "scissors":
      print(f"You picked {user_choice.capitalize()} and the computer picked {computer_choice.capitalize()}")
      print("Computer Wins")
      computer_points += 1
      print(f"Score:\nYou: {user_points}\nComputer: {computer_points}\nTies: {tie_points}")
    elif computer_choice == "rock":
      print(f"You picked {user_choice.capitalize()} and the computer picked {computer_choice.capitalize()}")
      print("You Win")
      user_points += 1
      print(f"Score:\nYou: {user_points}\nComputer: {computer_points}\nTies: {tie_points}")

  if user_choice == "scissors":
    if computer_choice == "rock":
      print(f"You picked {user_choice.capitalize()} and the computer picked {computer_choice.capitalize()}")
      print("Computer Wins")
      computer_points += 1
      print(f"Score:\nYou: {user_points}\nComputer: {computer_points}\nTies: {tie_points}")
    elif computer_choice == "paper":
      print(f"You picked {user_choice.capitalize()} and the computer picked {computer_choice.capitalize()}")
      print("You Win")
      user_points += 1
      print(f"Score:\nYou: {user_points}\nComputer: {computer_points}\nTies: {tie_points}")