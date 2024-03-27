from colorama import Fore
import datetime
from requests import get
from enchant import Dict

# Define functions to set colors
green = Fore.GREEN
yellow = Fore.YELLOW
red = Fore.RED
reset = Fore.RESET


# Define a function to get the date to use for the Wordle API
def get_date(date):
    min_date = datetime.date(2021, 6, 19)

    if date == 'today':
        return datetime.date.today().strftime('%Y-%m-%d')
    else:
        try:
            parsed_date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
            if parsed_date < min_date:
                return False

            max_days = {
                1: 31,  # January
                2: 29 if parsed_date.year % 4 == 0 and (
                            parsed_date.year % 100 != 0 or parsed_date.year % 400 == 0) else 28,  # February
                3: 31,  # March
                4: 30,  # April
                5: 31,  # May
                6: 30,  # June
                7: 31,  # July
                8: 31,  # August
                9: 30,  # September
                10: 31,  # October
                11: 30,  # November
                12: 31  # December
            }
            if parsed_date.day > max_days[parsed_date.month]:
                return False
            return parsed_date.strftime('%Y-%m-%d')
        except ValueError:
            return False


# Define a function to get a Wordle answer for the Wordle API based on a yyyy-mm-dd format
def get_wordle_answer(date):
    try:
        url = f"https://www.nytimes.com/svc/wordle/v2/{date}.json"
        response = get(url).json()
        return response["solution"]
    except:
        return False


# Define a function to print a colorful title for the command line
def print_title():
    print(green + "W" + yellow + "O" + red + "R" + green + "D" + yellow + "L" + red + "E" + reset)


# Define a function to assign a color to each letter in a word using its relation to the letters in the answer
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

    # Check if all letters are green
    if all(value == "GREEN" for value in letters.values()):
        return 1
    else:
        return letters


# Define a function to remove numbers from a string
def remove_numbers(string):
    return string.translate(str.maketrans('', '', '0123456789'))


# Define a function to print a hint based on the return value of check()
def print_hint(checked_dictionary):
    for letter, color in checked_dictionary.items():
        if color == "GREEN":
            print(green + remove_numbers(letter).upper(), end="")
        elif color == "YELLOW":
            print(yellow + remove_numbers(letter).upper(), end="")
        else:
            print(red + remove_numbers(letter).upper(), end="")
    print(reset + "")


# Define a function to check whether a string is a word or not
def is_word(word):
    d = Dict("en_US")
    return d.check(word)


# Define a function to display info about this game
def print_info():
    print(green + "Currently, there is no info to disclose (unfinished)" + reset)
