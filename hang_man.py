# text version of hangman with sound
# Author: Phil St Croix
# Written: Feb 28, 2023

import time
import winsound
import hangman_word as HW
import hangman_draw as HD

print()
print("\nWelcome to PHIL's text HANGMAN game with audio!")
print("Good Luck!")
print()

def main():

    # initialize the game
    guesses = set()
    word = HW.getChoice()
    max_attempts = 7
    lives = max_attempts
    hangDraw = HD.draw_hangman(lives)

    # play suspense sound at start of every guess
    winsound.PlaySound("suspense.wav", winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)

    # loop until user wins or losses
    while True:
        # show the word as underscores for unknown characters and filled-in letters for correct guess
        display_word = ''.join(letter if letter in guesses else '_' for letter in word)
        print(display_word)

        # ask user to guess a letter and validate it
        user_letter = input("Guess a letter: ")
        if len(user_letter) != 1 or not user_letter.isalpha():
            print("Invalid input.  Please enter a single letter.")
            continue
        if user_letter in guesses:
            print("You already guessed that letter.  Please try again.")
            continue
        if user_letter in word:
            print("Correct guess that letter is in the word!")
            winsound.PlaySound("Correct.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
            time.sleep(4)
            winsound.PlaySound("suspense.wav", winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)

        # add user guess to set of guesses
        guesses.add(user_letter)

        # check if won or lost
        if set(word) <= guesses:
            print("Congratulations, you won!")
            print("The word was", word + "!")
            break
        else:
            if user_letter not in word:
                lives -= 1
                print("Incorrect guess.  You have", lives, "lives remaining.")
                HD.draw_hangman(lives)
                # play wrong guess sound
                winsound.PlaySound("wrong.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
                time.sleep(4)
                winsound.PlaySound("suspense.wav", winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)
            if lives <= 0:
                print("Sorry, you lost.  The word was", word + ".")
                winsound.PlaySound(None, winsound.SND_FILENAME)
                time.sleep(4)
                winsound.PlaySound("suspense.wav", winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)
                break

    while True:
        play_again = input("Do you want to play again? (Y)es or (N)o: ").upper()
        if play_again == "Y":
            print("starting a new game...")
            main()
        elif play_again == "N":
            print("Thanks for playing!")
            exit()
        else:
            print("Invalid input.  Please enter (y)es or (n)o.")

if __name__ == "__main__":
    main()