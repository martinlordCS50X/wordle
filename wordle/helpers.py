from colorama import Fore
from enchant import Dict
import datetime


def validate_date(date_text):
    """
    Validates the format of a date string.

    Args:
    - date_text (str): The date string to be validated.

    Returns:
    - bool: True if the date string is in the format 'YYYY-MM-DD', False otherwise.
    """
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
        return True
    except ValueError:
        return False


def print_introduction():
    """
    Prints the introduction and rules of the word-guessing game.
    """
    print(Fore.GREEN + "W" + Fore.YELLOW + "O" + Fore.RED + "R" + Fore.GREEN + "D" + Fore.YELLOW + "L" + Fore.RED + "E")
    print(Fore.GREEN + "Guess a word and use this key as a hint to what the word is:")
    print("1. A letter being green means that that is the correct place for that letter to be.")
    print("2. A letter being yellow means it is in the word, but not in that place.")
    print("3. A letter being red means it is not in that word.")


def check(word, answer):
    """
    Compares a guessed word with the correct answer and generates a dictionary indicating the correctness of each letter position.

    Args:
    - word (str): The guessed word.
    - answer (str): The correct answer word.

    Returns:
    - dict: A dictionary where keys represent letters in the word along with their positions, and values represent the color code ('GREEN', 'YELLOW', or 'RED').
    """
    letters = {}
    _word = word.lower()
    _answer = answer.lower()
    for i, letter in enumerate(_word):
        if letter == _answer[i]:
            letters[f"{letter}{i}"] = "GREEN"
        elif letter in _answer:
            letters[f"{letter}{i}"] = "YELLOW"
        else:
            letters[f"{letter}{i}"] = "RED"
    return letters


def print_hint(checked_dictionary):
    """
    Prints hints for the word-guessing game based on the provided dictionary of letters and their colors.

    Args:
    - checked_dictionary (dict): A dictionary where keys represent letters in the word along with their positions, and values represent the color code ('GREEN', 'YELLOW', or 'RED').
    """
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
    """
    Checks if a given word exists in the English dictionary.

    Args:
    - word (str): The word to be checked.

    Returns:
    - bool: True if the word exists in the dictionary, False otherwise.
    """
    d = Dict("en_US")
    return d.check(word)


def remove_numbers(letter):
    """
    Removes any numerical digits from the input letter.

    Args:
    - letter (str): The letter from which numerical digits should be removed.

    Returns:
    - str: The letter with numerical digits removed.
    """
    return letter.translate(str.maketrans('', '', '0123456789'))
