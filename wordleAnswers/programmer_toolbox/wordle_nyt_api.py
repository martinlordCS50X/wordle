import datetime
from requests import get
from wordle_toolbox import red


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


if __name__ == "__main__":
    # Prompt the user for a date
    date = None
    while True:
        date = input("Please enter a date in yyyy-mm-dd format or 'today' for the answer: ").lower()
        if get_date(date):
            date = get_date(date)
            break
        else:
            print("Invalid date.", end=" ")
    print(f"Getting answer for {date}...")
    answer = get_wordle_answer(date)
    if not answer:
        print(red + "There was an error while getting the answer. Turn on your internet and try again.")
        exit()
    print(f"Answer for {date}'s Wordle according to The NYT: {get_wordle_answer(date)}")