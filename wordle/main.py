from helpers import print_introduction, check, print_hint, is_word
from colorama import Fore

print_introduction()
for _ in range(5):
    word = ""
    while len(word) != 5 or not is_word(word):
        word = input(Fore.RESET + "Enter a 5-letter word: ")

    checked_dictionary = check(word.lower())
    if checked_dictionary == 1:
        print(Fore.GREEN + "Y" + Fore.YELLOW + "O" + Fore.RED + "U " + Fore.GREEN + "W" + Fore.YELLOW + "O" + Fore.RED + "N" + Fore.GREEN + "!")
        exit()
    print_hint(checked_dictionary)

print("YOU LOST :(")