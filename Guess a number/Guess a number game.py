#import module
import random

#assign value to a
a = random.randint(1, 9)

#set boolean
exit = False
#begin loop
while(not exit):
	#define input
	guess = int(input("Please guess a number between 1 and 9: "))
	



	if guess == a:
		print("You guessed correctly! ")
	else:
		print("Sorry. You guess incorrectly.")

#ask users if they want to play again
	response = input("Do you want to play again? (Yes or No)")


	#Check answer
	if response == 'Yes':
		print("New game will begin.")
	elif response == 'No':
		exit = True
		print("Game over!")
	else:
		print("Inavlid input. Please type 'Yes' or 'No'. ")