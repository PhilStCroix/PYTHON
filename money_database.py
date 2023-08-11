# program for using a text file as a database
# for money to be used in my blackjack game
# Author: Phil St Croix
# Written: Feb 27/23

# let's try to open the text file to view its contents
def viewMoney():
    try:
        with open("money.txt", "r") as file:
            money = float(file.readline())
            money = round(money, 2)
        return money
    except:
        # if we get here there is no text file so lets make 1 with 1500 balance added
        print("'money.txt' not found.  Creating a new file with 1500 balance added.")
        with open("money.txt", "w", newline="") as file:
            file.write(str(1500))


def winMoney(bjWins):
    # used when we win
    startMoney = viewMoney()
    winMoney = startMoney + round(bjWins, 2)
    with open("money.txt", "w", newline="") as file:
        file.write(str(winMoney))


def betMoney(bjLoss):
    # used when we loose or actually when we bet(betting reduces our bank amount)
    startMoney = viewMoney()
    lossMoney = startMoney - bjLoss
    with open("money.txt", "w", newline="") as file:
        file.write(str(lossMoney))