# Rock, Paper, Scissors, Game for Beginners
# Follow @SudoJvck

import random

while True:
  def get_choices():
    player_choice = input("Enter a choice rock, paper, scissors: ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices
  
  def check_win(player, computer):
    print(f"You chose {player},Computer chose {computer}")
    if player == computer:
      return "It's a Tie!"
    elif player == "rock":
      if computer == "scissors":
        return "Rock smashes Scissors! You Win!" 
      else:
        return "Paper Smothers Rock. You Lose. :("
    elif player == "paper":
      if computer == "rock":
        return "Paper Smothers Rock. you Win!" 
      else:
        return "Scissors cuts Paper. You Lose. :(" 
    elif player == "scissors":
      if computer == "paper":
        return "Scissors cuts Paper! You Win!"
      else:
        return "Rock smashes scissors. You lose. :("
  
  choices = get_choices()
  results = check_win(choices["player"], choices["computer"])
  print(results)
  play_again = input("Would you like to play again? (y/n) ")
  if play_again.upper() == "Y":
    continue
  print("Bye..")
  break
