
#ask user for a word and give option to quit
word = input("Give me a word: ")

if word == word[::-1]:
	print(f"{word} is a palindrome! ")

else:
	print("Sorry , but this isn't a palindrome.")




