import random
from game_data import data
from art import logo, vs
import os

os.system('clear')
# to make it in a function

def clear():
     os.system('clear')


'''Randomizes the user options into two choices (later on)'''
def random_userOptions():
    return random.choice(data)

def formatData(data):
    name = data["name"]
    description = data["description"]
    country = data["country"]
    followers = data["follower_count"]
    # print(f'{name}: {account["follower_count"]}')
    return f"{name}, a {description}, from {country}, followers {followers}"

def checkFollowers(userInput, dataA, dataB):
    followerA = dataA['follower_count']
    followerB = dataB['follower_count']
    if userInput.lower() == 'a' and followerA > followerB or \
     userInput.lower() == 'b' and followerB > followerA:
        return True
    else:
        return False



def hlgame():
    score = 0
    game = True    
    dataA = random_userOptions()
    dataB = random_userOptions()
    while game:
        print(f"Score: {score}")
        print(logo)

        dataA = dataB
        dataB = random_userOptions()
        while dataA == dataB:
            dataB = random_userOptions()
                
        print(f"Choice A: {formatData(dataA)}") #Follower count for debugging, remove when done
        print(vs)
        print(f"Choice B: {formatData(dataB)}") #Follower count for debugging, remove when done

        userInput = input("\nWho has more followers ? Type 'A' or 'B' \n")
           

        result = checkFollowers(userInput, dataA, dataB)
        
        
        clear()

        """The loop that ends or continues the game"""
        if result is True:
            score += 1
        else:
            game = False
            print(f"- Incorrect, Good Luck next time. - \n  Final Score: {score}")


hlgame()