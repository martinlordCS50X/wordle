from nyt_api import answer
from colorama import Fore
from enchant import Dict

def print_introduction():
    print(Fore.GREEN + "W" + Fore.YELLOW + "O" + Fore.RED + "R" + Fore.GREEN + "D" + Fore.YELLOW + "L" + Fore.RED + "E")
    print(Fore.GREEN + "Guess a word and use this key as a hint to what the word is:")
    print("1. A letter being green means that that is the correct place for that letter to be.")
    print("2. A letter being yellow means it is in the word, but not in that place.")
    print("3. A letter being red means it is not in that word.")


def check(word):
    letters = {}
    for i, letter in enumerate(word):
        if letter in answer:
            if letter == answer[i]:
                letters[letter] = "GREEN"
            else:
                letters[letter] = "YELLOW"
        else:
            letters[letter] = "RED"
    if word == answer:
        return 1
    else:
        return letters


def print_hint(checked_dictionary):
    print("Answer: ", end="")
    for letter in checked_dictionary:
        if checked_dictionary[letter] == "GREEN":
            print(Fore.GREEN + letter, end="")
        elif checked_dictionary[letter] == "YELLOW":
            print(Fore.YELLOW + letter, end="")
        else:
            print(Fore.RED + letter, end="")
    print("")


def is_word(word):
    d = Dict("en_US")
    return d.check(word)
