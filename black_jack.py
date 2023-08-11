# this is the main black jack program to play a text version of black jack
# Auther: Phil St Croix
# Written: Feb 27, 2023

import card_deck as CD
import money_database as DB
import play_game as PG
import random

def main():
    # make a new deck of cards
    deck = CD.makeCards()
    print("\nWelcome to PHIL's text BLACK JACK game!")
    print("Black Jack Payout is 3:2")
    print("You're available money: " + str(DB.viewMoney()))
    if DB.viewMoney() <= 4:
        getMoney = PG.getMoney()

    while True:
        choice = PG.getChoice()
        wager = PG.getWager()
        playerCards = PG.playerCards(deck)
        dealerCards = PG.dealerCards(deck)
        playerScore = PG.getScores(playerCards)
        dealerScore = PG.getScores(dealerCards)
        print("\nDEALERS CARDS:")
        print(dealerCards[0][1], dealerCards[0][0])
        print("?  ???")
        print("\nYOUR CARDS:")
        for card in playerCards:
            print(card[1], card[0])

        # deal with double aces being dealt
        if len(playerCards) == 2:
            if playerCards[0][2] == 11 and playerCards[1][2] == 11:
                playerCards[0][2] = 1
                playerScore -= 10

        if len(dealerCards) == 2:
            if dealerCards[0][2] == 11 and dealerCards[1][2] == 11:
                dealerCards[0][2] = 1
                dealerScore -= 10

        if playerScore == 21:
            print("BLACKJACK you Win!")
            bjWin = DB.winMoney(wager * 1.5)
            continue

        while playerScore <= 21:
            playerChoice = input("\n(H)it or (S)tand>>>").upper()
            if playerChoice != "H" and playerChoice != "S":
                print("You must enter either 'H' or 'S'")
            elif playerChoice == "H":
                playerCard = random.choice(deck)
                playerCards.append(playerCard)
                deck.remove(playerCard)
                playerScore = PG.getScores(playerCards)
                if playerScore > 21:
                    for card in playerCards:
                        if card[2] == 11:
                            card[2] = 1
                            playerScore -= 10
                for card in playerCards:
                    print(card[1], card[0])
            else:
                print("\nDEALERS CARDS")
                for card in dealerCards:
                    print(card[1], card[0])
                break
            if playerScore > 21:
                print("YOU BUSTED!")
                break

        while dealerScore <= 16 and playerScore <= 21:
            print("DEALER MUST HIT")
            dealerCard = random.choice(deck)
            dealerCards.append(dealerCard)
            deck.remove(dealerCard)
            input("Press enter to continue>>>")
            print(dealerCard[1], dealerCard[0])
            dealerScore = PG.getScores(dealerCards)
            if dealerScore > 21:
                for card in dealerCards:
                    if card[2] == 11:
                        card[2] = 1
                        dealerScore -= 10

        if dealerScore == 21:
            print("DEALER HAS BLACKJACK")
        if dealerScore > 21:
            print("DEALER BUSTED")
        if playerScore == 21:
            print("\nYou got BlackJack!")

        print()
        print("Players Score is " + str(playerScore))
        print("Dealers Score is " + str(dealerScore))
        didWin = PG.checkForWin(playerScore, dealerScore)
        if didWin == 1:
            bjWin = DB.winMoney(wager * 1.5)
        if didWin == 0:
            bjWin = DB.winMoney(wager)
        print("Your Available Money: " + str(DB.viewMoney()))
        if DB.viewMoney() <= 4:
            print("YOU HAVE BEEN BANKRUPTED! GOOD THING YOU WEREN'T PLAYING FOR REAL MONEY!")
            getMoney = PG.getMoney()

        if len(deck) <= 26:
            print("\nHalf deck used, dealer is reshuffling...")
            deck = CD.makeCards()
            input("Deck shuffled press enter to continue>>>")

if __name__ == "__main__":
    main()