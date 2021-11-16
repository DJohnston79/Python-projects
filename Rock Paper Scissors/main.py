#Remember the rules:
#Rock beats scissors
#Scissors beats paper
#Paper beats rock

from random import randint

#create a list of play options
moves = ["rock", "paper", "scissors"]

#assign a random play to the computer
computer = moves[randint(0,2)]

#begin game 
stop = False

while(not stop):
	player1 = input("Choose: rock, paper, scissors: ")
	if player1 == computer:
		print("It's a tie!")
	elif player1 == 'rock' and computer == 'scissors':
		print("Rock beats scissors. Player 1 wins")
	elif player1 == 'scissors' and computer == 'paper':
		print("Scissors beats paper.Player 1 wins")
	elif player1 == 'paper' and computer == 'rock':
		print("Paper beats rock! Player 1 wins")
	elif computer == 'rock' and player1 == 'scissors':
		print("Rock beats scissors. The computer wins!")
	elif computer == 'scissors' and player1 == 'paper':
		print("scissors beats paper. The computer wins!")
	elif computer == 'paper' and player1 == 'rock':
		print("Paper beats rock. The computer wins!")
	else:
		print("Wrong input. Please enter 'rock', 'paper', or 'scissors'. ")

	#ask users if they want to play again
	response = input("Do you want to play again? (Yes or No)")


	#Check answer
	if response == 'Yes':
		print("New game will begin.")
	elif response == 'No':
		stop = True
		print("Game over!")
	else:
		print("Invalid input. Please type 'Yes' or 'No'. ")






