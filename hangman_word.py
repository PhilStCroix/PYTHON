# this is gonna handle users difficulty choose and pick a random word from words_alpha.txt
# Author: Phil St Croix
# Written Feb 28, 2023

import random

def getChoice():
    # read the list of words from the file
    with open("words_alpha.txt", "r") as word_file:
        words = list(word_file.read().split())

    # define the difficulty levels
    easy_words = [word for word in words if 3 <= len(word) <= 4]
    medium_words = [word for word in words if 5 <= len(word) <= 7]
    hard_words = [word for word in words if len(word) >= 8]

    # ask user to select difficulty
    print("HangMan has 3 difficulty levels:")
    print("1 - Easy")
    print("2 - Medium")
    print("3 - Hard")

    while True:
        try:
            level = int(input("Enter your choice (1, 2 or 3): "))
        except:
            print("Choice is invalid - try again")
        else:
            if level in [1, 2, 3]:
                break
            else:
                print("Invalid choice.  Please enter 1, 2 or 3.")

    # select random word based on difficulty
    if level == 1:
        word = random.choice(easy_words)
    elif level == 2:
        word = random.choice(medium_words)
    else:
        word = random.choice(hard_words)
    return word