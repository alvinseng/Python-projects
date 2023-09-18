import random
from hangman_art import stages
from hangman_art import logo
from hangman_words import word_list
from replit import clear

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(logo)

#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
	display += "_"

prev_guess = []

while not end_of_game:
	guess = input("Guess a letter: ").lower()

	clear()
	
	#Check guessed letter
	for position in range(word_length):
		letter = chosen_word[position]
		#print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
		if letter == guess:
			display[position] = letter

	if guess not in prev_guess:
		prev_guess += guess
	elif guess in prev_guess:
		print(f"{guess} has already been guessed. Try again.")
		continue 
			
	#Check if user is wrong.
	if guess not in chosen_word:
		lives -= 1
		if lives == 0:
			end_of_game = True
			print("You lose.")

	#Join all the elements in the list and turn it into a String.
	print(f"{' '.join(display)}")

	#Check if user has got all letters.
	if "_" not in display:
		end_of_game = True
		print("You win.")

	print(stages[lives])
	print(prev_guess)

