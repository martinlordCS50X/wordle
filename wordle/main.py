import datetime
from helpers import print_introduction, check, print_hint, is_word, validate_date
from colorama import Fore

# Print introduction and rules
print_introduction()

# Prompt the user for a date
while True:
    user_input = input(Fore.RESET + "Enter a date (yyyy-mm-dd) or 'today' for today's Wordle answer: ").strip().lower()
    if user_input == 'today':
        date = datetime.date.today()
        break
    elif validate_date(user_input):
        date = user_input
        break
    else:
        print("Invalid date format. Please enter a date in the format 'yyyy-mm-dd' or 'today'.")

# Fetch the Wordle answer based on the date
if user_input == 'today':
    from nyt_api import answer
else:
    from nyt_api import get_wordle_answer
    answer = get_wordle_answer(date)

# Main game loop
for _ in range(6):
    word = ""
    while len(word) != 5 or not is_word(word):
        word = input(Fore.RESET + "Enter a 5-letter word: ").lower()

    checked_dictionary = check(word.lower(), answer)
    if checked_dictionary == 1:
        print(Fore.GREEN + "Y" + Fore.YELLOW + "O" + Fore.RED + "U " + Fore.GREEN + "W" + Fore.YELLOW + "O" + Fore.RED + "N" + Fore.GREEN + "!")
        exit()
    print_hint(checked_dictionary)

print("YOU LOST :(")
