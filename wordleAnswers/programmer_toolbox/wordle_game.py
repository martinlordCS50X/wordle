from wordle_toolbox import green, yellow, red, reset, get_date, get_wordle_answer, print_title, check
from wordle_toolbox import is_word, print_hint, print_info

# Print the title of the game
print_title()

# Display some info
print(green + "Please play Wordle if you haven't already. At any time, type 'info' for info.")
print("We are getting answers from the New York Times Wordle API." + reset)

# Prompt the user how many guesses they want
while True:
    user_input = input("How many guesses do you want (1-20 inclusive)? ")
    if user_input.strip() == "":
        guess_count = 6
        break
    try:
        guess_count = int(user_input)
        if 1 <= guess_count <= 20:
            break
        else:
            print("Please enter a number between 1 and 20.")
    except ValueError:
        print("Please enter a valid integer.")

# Prompt the user for a date
date = None
while True:
    date = input("Please enter a date in yyyy-mm-dd format or 'today' for the answer: ").lower().strip()
    if get_date(date):
        date = get_date(date)
        break
    elif date == "info":
        print_info()
    else:
        print("Invalid date.", end=" ")

# Get an answer from the NYT API based on this date
print(f"Getting answer for {date}...")
answer = get_wordle_answer(date)
if not answer:
    print(red + "There was an error while getting the answer. Turn on your internet and try again.")
    exit()

# Prompt the user if they want to know the answer
reveal_answer = input(red + "Would you like to know the answer? (y/n): ").lower().strip()
if reveal_answer.startswith("y"):
    print(f"The answer is '{answer}'")
print("" + reset, end="")

# Main game loop
for _ in range(guess_count):
    guess = input(f"{guess_count - _} guesses left. Guess: ").lower().strip()
    while len(guess) != 5 or not is_word(guess):
        guess = input(f"Not a 5 letter word. Try again: ")

    checked_guess = check(guess, answer)
    if checked_guess == 1:
        print(green + "Y" + yellow + "O" + red + "U " + green + "W" + yellow + "O" + red + "N" + green + "!")
        exit()
    print_hint(checked_guess)

print(red + "YOU LOST!")