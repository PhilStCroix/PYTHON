# program to build a deck of cards
# Author: Phil St Croix
# Written: Feb 27, 2023

def makeCards():
    # make 4 lists to build the deck
    # 1st start with the four suits
    suits = ["♣", "♥", "♠", "♦"]
    # now the card ranks
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    # and then the card values for each rank
    values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

    # the 4th list is for the deck and starts empty
    deck = []
    # start with a loop thru the suits
    for suit in suits:
        counter = 0
        # Now a nested loop to go thru ranks
        for rank in ranks:
            # create a new card for each iteration of the loop
            newCard = []
            newCard.append(suit)
            newCard.append(rank)
            newCard.append(values[counter])
            # now append the new card to the deck
            deck.append(newCard)
            counter += 1
    return deck