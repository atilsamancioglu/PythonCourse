name = input("Name: ")
print("Hello " + name + " time to play hangman!")

secret_word = "Metallica"

guesses = ""

lives = 10

while lives > 0:

	character_left = 0

	for character in secret_word:

		if character in guesses:

			print(character)
		else:
			print("-")
			character_left += 1

	if character_left == 0:
		print("You won!!!")	
		break


	guess = input("Guess a word: ")
	guesses += guess

	if guess not in secret_word:
		lives -= 1
		print("Wrong!")
		print(f"You have {lives} left")

		if lives == 0:
			print("You died!")

