from importlib import import_module
from data import title, you_win, you_loose
import os, random

def game(player_list, target):
    y = 0
    x = 1
    hanged = "#-HANGED-#"
    hanged = list(hanged)
    
    while x:
        os.system('cls')
        print (title)
        print (" ".join(player_list)) #Show the _ _ _ to guess the word
        print (" ".join(hanged[:y:])) #Show text: #-HANGED-# progressively if you fail one letter
        if player_list == target:
            print (you_win)
            break
        letter = input(str("Insert a letter and press enter: "))
        if letter in target:
            for i in range(len(target)):
                if target[i] == letter:
                    player_list.pop(i) #clear underscore in that position
                    player_list.insert(i, letter) #...put correct letter instead
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
    player_list = ["_" for i in range(len(target))] #Create the _ _ _
    game(player_list, target)

    
if __name__ == '__main__':
    run()