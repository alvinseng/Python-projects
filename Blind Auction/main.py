from replit import clear
from art import logo

print(logo)
print("Welcome to the Silent Auction! To start... \n")
   
biddingList = []

 # collecting auction data 
def biddingWar(bidder, bidding):
    newBidder = {}
    newBidder["User"] = bidder
    newBidder["Bid"] = bidding
    biddingList.append(newBidder)
    
auctionTime = True
while auctionTime == True:
    # user input for bidding 
    userInput = input("What is your name? \n")
    biddingAmount = int(input("How much are you bidding? $ \n"))
    additionalBidder = input("Are there anymore Bidders? 'y/n' \n")
    
    biddingWar(userInput, biddingAmount)
    # Sorting from high to low
    highestBidder = sorted(biddingList, key=lambda x: x["Bid"], reverse=True)
    winner = highestBidder[0]['User']
    
    if additionalBidder == 'no':
        auctionTime = False
        clear()
        print("Thank You for Coming...\n")
        # print winnder and bid value
        print(f"The winner is {winner} at ${highestBidder[0]['Bid']}.")
    else:
        clear()



