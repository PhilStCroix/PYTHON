# this will draw the hangman board as the user plays
# Author: Phil St Croix
# Written: Feb 28, 2023

def draw_hangman(lives):
    if lives ==7:
        print("   ______")
        print("   |")
        print("   |")
        print("   |")
        print("   |")
        print("   |")
        print("   ------")
    elif lives == 6:
        print("   ______")
        print("   |    |")
        print("   |")
        print("   |")
        print("   |")
        print("   |")
        print("   ------")
    elif lives == 5:
        print("   ______")
        print("   |    |")
        print("   |    0")
        print("   |")
        print("   |")
        print("   |")
        print("   ------")
    elif lives == 4:
        print("   ______")
        print("   |    |")
        print("   |    0")
        print("   |    |")
        print("   |")
        print("   |")
        print("   ------")
    elif lives == 3:
        print("   ______")
        print("   |    |")
        print("   |    0")
        print("   |   /|")
        print("   |")
        print("   |")
        print("   ------")
    elif lives == 2:
        print("   ______")
        print("   |    |")
        print("   |    0")
        print("   |   /|\\")
        print("   |")
        print("   |")
        print("   ------")
    elif lives == 1:
        print("   ______")
        print("   |    |")
        print("   |    0")
        print("   |   /|\\")
        print("   |   / ")
        print("   |")
        print("   ------")
    elif lives == 0:
        print("   ______")
        print("   |    |")
        print("   |    0")
        print("   |   /|\\")
        print("   |   / \\")
        print("   |")
        print("   ------")