"""
-------------------------------------------------------
| Written by Joseph Mercer; released to public domain |
-------------------------------------------------------
"""


import random
import os
import time
import sys

os.system("clear")

HANGMAN = ["""






           ""","""
________
|/     |
|      0
|     /|\\
|      |
|     /
|__________
""","""
________
|/     |
|      0
|     /|\\
|      |
|
|__________
""","""
________
|/     |
|      0
|     /|
|      |
|
|__________
""","""
________
|/     |
|      0
|      |
|      |
|
|__________
""","""
________
|/     |
|      0
|
|
|
|__________
""","""
________
|/     |
|
|
|
|
|__________
""","""
________
|/     
|
|
|
|
|__________
"""]


hard=False
normal=False
easy=False

def showBanner():
    print(" _   _                                              ________   ")
    print("| | | |                                             |/     |   ")
    print("| |_| | __ _ _ __   __ _ _ __ ___   __ _ _ __       |      0   ")
    print("|  _  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \      |     /|\  ")
    print("| | | | (_| | | | | (_| | | | | | | (_| | | | |     |      |   ")
    print("\_| |_/\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|     |     / \  ")
    print("                    __/ |                           |__________")
    print("                   |___/                                       ")
    print("\nA command line game created by @jmrcr.\n")

def showHangman(HANGMAN, lives):
    print(HANGMAN[lives])


def difficulty():        #    This function decides which txt file it pulls a word from. Change this so that all words are in one file.
    diff=" "

    os.system("clear")
    while diff:
        global hard
        global normal
        global easy

        diff=input("Please select your difficulty setting:\n\n        Hard - Normal - Easy\n\n")
        if diff.upper()== "HARD":
            hard=True
            randWordGen()
            return
        elif diff.upper()== "NORMAL":
            normal=True
            randWordGen()
            return
        elif diff.upper()== "EASY":
            easy=True
            randWordGen()
            return
        elif diff.upper()== "BACK":
            begin()
            return
        else:
            os.system("clear")
            print("Unknown option")
            time.sleep(2)
            os.system("clear")

def randWordGen():       #   Function uses the random module to pick a word from the precified txt file.
    os.system("clear")
    if hard==True:
        randWord = random.choice(open("/home/a/Documents/Hangman/10word.txt").read().split())
        startGame(randWord)
    elif normal==True:
        randWord = random.choice(open("/home/a/Documents/Hangman/5word.txt").read().split())
        startGame(randWord)
    elif easy==True:
        randWord = random.choice(open("/home/a/Documents/Hangman/3word.txt").read().split())
        startGame(randWord)
    else:
        print("ERROR")

def startGame(randWord):    #   Import the random word variable from above function.
    a = list(randWord)      #   Turns the random word into a list
    correct = list()        #   List to add correct inputs from user too
    incorrect = list()
    global hard,normal,easy            #    Carrying the global difficulty variables into this function so correct unknown spaces are used **Not complete**
#    print(len(a))              #   Testing lines
#    print(a)
#    print(a[1])
    lives = len(HANGMAN) - 1
    blanks = "_" * len(randWord)

    while (lives > 0):             #   Recursive while loop, nested if statements used to decrese lives left or determine a win
        showHangman(HANGMAN, lives)
        guess = input("Have a guess:")
        if len(guess) != 1:
            print("Please enter a single letter!\n")
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print("Please enter an alphabetic character!")
        else:
            if guess in a:
                if guess not in correct:
                    correct.append(guess)       #    Adds the guess varible to the correct list if it meets all the conditions
#                    print(correct)
                    for i in range(len(randWord)):      #   Replaces blanks with correct guesses
                        if randWord[i] in correct:
                            blanks = blanks[:i] + randWord[i] + blanks[i+1:]
                    for letter in blanks:
                        print(letter, end='')
                    print()
                    print("Well done! Lives remaining:",lives)
                    if set(a).issubset(correct):        #   Checks if list(correct) contains all the characters used in randWord
                            win()
                            return
                else:
                    print("You have already input this character!")
            else:
                if guess not in incorrect:
                    incorrect.append(guess)
                    lives=lives-1
                    print("Incorrect, you have",lives,"lives left :(")
                else:
                    print("You have already input this character!")

    os.system("clear")
    print("""
________
|/     |
|      0
|     /|\\
|      |
|     / \\
|__________
""")
    loser=input("The correct word was '{0}'. \nYou have lost, would you like to play again? (Y/n)\n".format(randWord))     #   Using the str.format to have multiple arguments in an input
    if loser.upper() == "Y":
        hard=False
        normal=False
        easy=False
        begin()
    elif loser.upper() == "N":
        sys.exit()

def win():
    global hard,normal,easy
    if hard == True:
        difficulty = "hardest"
    elif normal == True:
        difficulty = "most mediocre"
    elif easy == True:
        difficulty = "easiest"

    again=input("\nWinner!!! Congratulations you beat the {0} level!\n\nTest your mind and try again?(Y/n)".format(difficulty))
    if again.upper() == "Y":
        begin()
    elif again.upper() == "N":
        sys.exit()

def instructions():     #   Simply an instrutions page for those less informed
    menu=input("""Welcome to my hangman game, I have written this in python.

To play the game you simply need to type '1' in order to initiate the game.
After this you will be prompted to choose a difficulty. Select the desired
diffiulty level by typing it into the command line. Depending on your
chosen difficulty level a random word of corresponding difficulty will be
selected. From here you must try and guess said word correctly, letter by
letter before your lil stick man kicks the bucket..

Good luck

To go back to the menu just type 'Back'

""")
    if menu.upper() == "BACK":
        begin()
    else:
        print("Unknown Option")
        time.sleep(1)
        os.system("clear")
        instructions()

def begin():        #   The script's first function that runs, menu for the front page
    os.system("clear")
    if __name__=="__main__":
        option=" "
        target=None
        showBanner()
        while not option[0] in ["q","Q"]:
            print("\n 1. Play game")
            print("\n 2. How to Play")
            print("\n Q. Quit")

            option=input("\n Choose an option: ")
            os.system("clear")
            if option[0] == "1":
                difficulty()
                return
            elif option[0] == "2":
                instructions()
                return
            elif option[0] in ["Q","q"]:
                break
            else:
                print("Unknown option\n\n")
begin()
