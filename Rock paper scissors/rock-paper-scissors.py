import random


possible_inputs = ["fire", "rock", "gun", "lightning", "devil", "dragon", "water", "air", "paper",
                   "sponge", "wolf", "tree", "human", "snake", "scissors"]

name = input("Enter your name: > ")
print(f"Hello, {name}")

ratings = open('rating.txt', 'r')
ratings_list = ratings.read().split()

if name in ratings_list:
    index = ratings_list.index(name)
    score = ratings_list[index + 1]
else:
    score = 0

game_list = input("You can add your game options splitted with commas\n>\n").split(",")
if game_list == ['']:
    game_list = ['rock', 'paper', 'scissors']
print("Okay, let's start")
while True:
    selection = input("Type your guess, !exit for exit or !rating for your score.")
    pc_selection = random.choice(game_list)
    if selection == "!exit":
        print("Bye!")
        break
    elif selection == "!rating":
        print(f"Your rating: {score}")
    elif selection not in game_list:
        print("Invalid input")
    else:
        _ind = game_list.index(selection)
        list_options = game_list[_ind + 1:] + game_list[:_ind]
        if pc_selection == selection:
            print(f"There is a draw ({pc_selection})")
            score += 50
        elif pc_selection in list_options[int(len(list_options) / 2):]:
            print(f"Well done. Computer chose {pc_selection} and failed")
            score += 100
        else:
            print(f"Sorry, but computer chose {pc_selection}")
