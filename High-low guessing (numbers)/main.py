from art import logo
import random


# print(numGen) 
"""generates number randomly/ dubug to know what number prints"""

numGen = random.randint(0, 101)
life = 0
game = False

"""slecting difficulty level"""
def difficulty():
    global life
    userInput = input("\nEasy or Hard? ")
    if userInput.lower() == "easy":
        life += 10
    elif userInput.lower() == "hard":
        life += 5
    print(f'\nLife: {life}') #player's life
    
"""letting player know if guess is high or low """
def highLow():
    global game
    global life
    userGuess = int(input("\nWhat is your guess? "))
    if userGuess > 100:
        return "Please guess between 0 - 100"
    if life == 0 or userGuess == numGen:
        game = True
        return f"\nThe number was {numGen}"
    elif userGuess > numGen:
        life -= 1
        print(f'\nLife: {life}') #player's life
        return "High"
    elif userGuess < numGen:
        life -= 1
        print(f'\nLife: {life}') #player's life
        return "Low"

"""Prints the intro"""
def intro():
    print(logo)
    print("""
Welcome to the Number Guessing Game
I'm thinking of a number between 1 - 100.
Give me your best guess...""")

def guessingGame():
    intro()
    difficulty()
    while not game:
        print(highLow())

guessingGame()
