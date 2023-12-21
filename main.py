from termcolor import colored
import random
import time
import sys

def write(text, speed=0.037):
  for char in text:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(speed)

# Variables and Dictionaries
choose_difficulty = colored('Would you like to play normal or hard mode? \n', 'dark_grey')
choose_card = colored('Choose rock, paper, or scissors \n', 'dark_grey')

win = colored('You win!', 'green')
lose = colored('You lost!', 'red')
Draw = colored('It is a draw!', 'yellow')

player_deck = ['rock', 'paper', 'scissors']
enemy_deck = ['rock', 'paper', 'scissors']

hard_rock_enemy_deck = ['rock', 'rock', 'rock', 'rock', 'paper', 'scissors']
hard_paper_enemy_deck = ['paper', 'paper', 'paper', 'paper', 'rock', 'scissors']
hard_scissors_enemy_deck = ['scissors', 'scissors', 'scissors', 'scissors', 'paper', 'rock']

# Checks to see if the player won
def Win_rock(player_card, enemy_card):
  if player_card == 'rock' and enemy_card == 'scissors':
    return True
  return False

def Win_paper(player_card, enemy_card):
  if player_card == 'paper' and enemy_card == 'rock':
    return True
  return False

def Win_scissors(player_card, enemy_card):
  if player_card == 'scissors' and enemy_card == 'paper':
    return True
  return False

def draw(player_card, enemy_card):
  if player_card == enemy_card:
    return True
  return False

# Print title
write(colored('ROCK PAPER SCISSORS GAME \n', 'dark_grey'))
print()

# Choose game difficulty
write(choose_difficulty)
game_difficulty = input('> ')
print()

# If player chose normal mode
if game_difficulty.lower() == 'normal' or 'normal mode' or 'normal-mode':
  Normal = True  # Change normal to true
  Hard = False   # Change hard to false

if game_difficulty.lower() == 'hard' or 'hard mode' or 'hard-mode':
  Normal = False
  Hard = True

if Normal == True:  # if normal == true
  write(choose_card)
  player_card = input('> ').lower()
  print()

  # Confirm player and opponent card draws
  if player_card in player_deck:
    enemy_card = random.choice(enemy_deck)

    # Show what card opponent chose
    write(colored(f'The opponent chose {enemy_card}!\n', 'dark_grey'))
    print()

    # Check if player won
    if Win_rock(player_card, enemy_card) or Win_paper(player_card, enemy_card) or Win_scissors(player_card, enemy_card):
      print(win)   # Prints this if they won
    elif draw(player_card, enemy_card):
      print(Draw)  # Prints this if it was a draw
    else:
      print(lose)  # Prints this if they lost

if Hard == True:
  write(choose_card)
  player_card = input('> ').lower()
  print()

  # Check to see if chosen card is valid
  if player_card in player_deck:
    try:

      # Get the hard-mode enemy card
      if player_card.lower() == 'rock':
        enemy_card = random.choice(hard_paper_enemy_deck)
      if player_card.lower() == 'paper':
        enemy_card = random.choice(hard_scissors_enemy_deck)
      if player_card.lower() == 'scissors':
        enemy_card = random.choice(hard_rock_enemy_deck)

      # Show what card opponent chose
      write(colored(f'The opponent chose {enemy_card}!\n', 'dark_grey'))
      print()

    except:
      print(colored('Something went wrong!', 'red'))
  else:
    print(colored('Not a valid option', 'red'))
  
  # Check if player won
  if Win_rock(player_card, enemy_card) or Win_paper(player_card, enemy_card) or Win_scissors(player_card, enemy_card):
    print(win)   # Prints this if they won
  elif draw(player_card, enemy_card):
    print(Draw)  # Prints this if it was a draw
  else:
    print(lose)  # Prints this if they lost
