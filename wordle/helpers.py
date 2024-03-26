from colorama import Fore
from enchant import Dict
import datetime


def validate_date(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
        return True
    except ValueError:
        return False


def print_introduction():
    print(Fore.GREEN + "W" + Fore.YELLOW + "O" + Fore.RED + "R" + Fore.GREEN + "D" + Fore.YELLOW + "L" + Fore.RED + "E")
    print(Fore.GREEN + "Guess a word and use this key as a hint to what the word is:")
    print("1. A letter being green means that that is the correct place for that letter to be.")
    print("2. A letter being yellow means it is in the word, but not in that place.")
    print("3. A letter being red means it is not in that word.")


def check(word, answer):
    # Check for special characters or spaces
    if not word.isalpha() or not answer.isalpha():
        return 0

    # Check for mismatched lengths
    if len(word) != len(answer):
        return 0

    letters = {}
    _word = word.lower()
    _answer = answer.lower()

    # Create a dictionary to store the positions of each letter in the answer
    answer_positions = {letter: [] for letter in _answer}
    for i, letter in enumerate(_answer):
        answer_positions[letter].append(i)

    # Iterate through each letter in the guess
    for i, letter in enumerate(_word):
        # Check if the letter is correct and in the correct position
        if letter == _answer[i]:
            letters[f"{letter}{i}"] = "GREEN"
        # Check if the letter is correct but in the wrong position
        elif letter in answer_positions:
            # Check all positions of the letter in the answer
            for pos in answer_positions[letter]:
                # If the position of the letter in the guess matches any position in the answer
                if pos != i:
                    letters[f"{letter}{i}"] = "YELLOW"
                    break
            else:
                # If the letter is not found in any other position in the answer
                letters[f"{letter}{i}"] = "RED"
        # If the letter is incorrect
        else:
            letters[f"{letter}{i}"] = "RED"

    return letters


def print_hint(checked_dictionary):
    print("Hint: ", end="")
    for letter, color in checked_dictionary.items():
        if color == "GREEN":
            print(Fore.GREEN + remove_numbers(letter).upper(), end="")
        elif color == "YELLOW":
            print(Fore.YELLOW + remove_numbers(letter).upper(), end="")
        else:
            print(Fore.RED + remove_numbers(letter).upper(), end="")
    print("")


def is_word(word):
    d = Dict("en_US")
    return d.check(word)


def remove_numbers(letter):
    return letter.translate(str.maketrans('', '', '0123456789'))
