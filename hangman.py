from importlib import import_module
from data import *
import os, random

def game(player_list, target):
    y = 0
    x = 1
    hanged = "#-HANGED-#"
    hanged = list(hanged)
    
    while x:
        os.system('cls') #Clear the terminal
        print (title)
        print (" ".join(player_list)) #Show the _ _ _ to guess the word
        print (" ".join(hanged[:y:])) #Show the _ _ _ when you loose the game
        if player_list == target:
            print (you_win)
            break
        letter = input(str("Insert a letter and press enter: ")) #ask for a letter
        if letter in target: #if letter exist (at least one occurrence)
            for i in range(len(target)): #we put any occurrence in every index
                if target[i] == letter:
                    player_list.pop(i) #clear the _
                    player_list.insert(i, letter) #put the letter instead
        else:
            y += 1
            if y == 12:
                print (you_loose)
                print ("Era "+str(target))
                break
        x += 1


def run():
    path = "./data.txt"
    with open(path, "r", encoding="utf-8") as f:
        word = [line.strip() for line in f]
    target = random.choice(word)
    target = list(target)
    player_list = ["_" for i in range(len(target))]
    game (player_list, target)

    
if __name__ == '__main__':
    run()