import random
import os
import time
import sys

os.system("clear")

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

def difficulty():        #    This function decides which txt file it pulls a word from. Change this so that all words are in one file.
    diff=" "

    os.system("clear")
    while diff:
        global hard
        global normal
        global easy

        diff=input("Please select your difficulty setting:\n\n        Hard - Normal - Easy\n\n")
        if diff== "Hard":
            hard=True
            randWordGen()
            return
        elif diff== "Normal":
            normal=True
            randWordGen()
            return
        elif diff== "Easy":
            easy=True
            randWordGen()
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
    correct = list()        #   List to add correctinputs from user too
    global hard,normal,easy            #    Carrying the global difficulty variables into this function so correct unknown spaces are used **Not complete**
#    print(len(a))              #   Testing lines
#    print(a)
#    print(a[1])
    lives = 6
    diffQuan = ""

    if hard==True:
        diffQuan="----------"
    elif normal==True:
        diffQuan="-----"
    elif easy==True:
        diffQuan="---"

    while (lives > 0):              #   Recursive while loop, nested if statements used to decrese lives left or determine a win
        guess = input("Have a guess:")
        if guess in a:
            if guess not in correct:
                correct.append(guess)       #    Adds the guess varible to the correct list if it meets all the conditions
                print(correct)
                print("Well done! Lives remaining:",lives)
                if set(a).issubset(correct):        #   Checks if list(correct) contains all the characters used in randWord
                        win()
                        return
            else:
                print("You have already input this character!")
        else:
            lives=lives-1
            print("Incorrect, you have",lives,"lives left :(")

    loser=input("The correct word was {0} \nYou have lost, would you like to play again? (Y/n)\n".format(randWord))     #   Using the str.format to have multiple arguments in an input
    if loser == "Y" or "y":
        hard=False
        normal=False
        easy=False
        begin()
    elif loser == "N" or "n":
        sys.exit()

def win():
    print("Winner")

def instructions():     #   Simply an instrutions page for those less informed
    menu=input("You're now reading the instructions\n\nTo go back to the menu just type 'Back'\n")
    if menu == "Back":
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
