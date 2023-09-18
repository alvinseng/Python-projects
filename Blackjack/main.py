from art import logo
import random
from replit import clear

deckValue = {
    'A' : 11,
    '2' : 2,
    '3' : 3,
    '4' : 4,
    '5' : 5,
    '6' : 6,
    '7' : 7,
    '8' : 8,
    '9' : 9,
    '10': 10,
    'J' : 10,
    'Q' : 10,
    'K' : 10
}

#deals the card out to the players
def dealCard():
    """returns 2 random cards from the deck to computer/player's Hand"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    #shuffling the keys and drawing 2 keys out of the list
    card = random.choice(cards)
    return card

#Calculates both the User & Computer scores to "21" / '0'
def calculateScore(hands):
    if len(hands) == 2 and sum(hands) == 21:
        return 0
    if sum(hands) > 21 and 11 in hands:
        hands.remove(11)
        hands.append(1)
    return sum(hands)

def compare(userScore,compScore):
    if userScore == compScore or (userScore > 21 and compScore > 21): 
        return "\nDraw"
    elif compScore == 0:
        return "\nComputer Wins"
    elif userScore == 0:
        return "\nPlayer Wins"
    elif userScore > 21:
        return "\nComputer Wins"
    elif compScore > 21:
        return "\nPlayer Wins"
    elif compScore > userScore and compScore <= 21:
        return "\nComputer Wins"
    elif userScore > compScore and userScore <= 21:
        return "\nPlayer Wins"
        
def playGame():


    #player's start hand
    userCards = []
    compCards = []
    
    for _ in range(2):
        userCards.append(dealCard())
        compCards.append(dealCard())
    
    print(logo)
    gameInput = input("Start Game? 'Y/N' \n")
    if gameInput.lower() == 'y':
        dealCard()
    
    """Initial card & score of both the computer and user """
    print(f'\nPlayer Cards : \n {userCards[0]}  {userCards[1]}')
    print(f'Computer Cards : \n {compCards[0]}  X')
    userScore = calculateScore(userCards)
    compScore = calculateScore(compCards)
    
    
    game_over = False
    """User loop to draw cards until bust or 21"""
    while not game_over:
        '''Score is over when over 21 or at 21'''
        if userScore == 0 or userScore > 21 or compScore == 0 :
            game_over = True
        else:
            hitC = input("\nWould you like another card?\n") # Player's input to gain a card
            if hitC.lower() == 'y':
                userCards.append(dealCard())
                userScore = calculateScore(userCards)
                print(f" {userCards}")
            else: 
                game_over = True
            
    while compScore < 17 and compScore != 0:
        compCards.append(dealCard())
        compScore = calculateScore(compCards)
    
    
    print(f"\nPlayer's Cards: {userCards} | score: {userScore} ") #outcome 
    print(f"Comp's Cards: {compCards} | score: {compScore}") #outcome
        
        
        
    calculateScore(userCards)
    calculateScore(compCards)
    print(compare(userScore, compScore))

"""Replay Game"""
playGame() #starts game
while input("\nPlay Again? 'Y' or 'N' ").lower() == 'y':
    clear()
    playGame()
