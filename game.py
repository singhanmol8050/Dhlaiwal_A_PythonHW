# import the random package so that we can generate a random choice
from random import randint

# choices is an array => an array is a container that can hold multiple values
#  arrays are 0-based -> first entry is 0, 2nd is 1, 3rd is 2 etc
choises = ["rock", "paper", "scissors"]

# set the computer variable to one of these choises (0, 1 or 2)
computer = choises[randint(0, 2)]

# set up the game loop so that we don't have to restart all the time
player = False

while player is False:
	#set player to True
    player = input("choose rock, paper or scissors\n")

    print("computer chose", computer, "\n")
    print("player chose", player, "\n")

    if computer =="quit":
    	exit()
	elif computer == player:
		print("tie! no one wins, play again")


	# need to check all our conditions after checking for a tie
	player == False
	computer = choices[randint(0, 2)]