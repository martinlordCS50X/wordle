import datetime
import requests


# Function to fetch Wordle answer for a given date
def get_wordle_answer(date):
    url = f"https://www.nytimes.com/svc/wordle/v2/{date}.json"
    response = requests.get(url).json()
    return response["solution"]


# Instantiate answer variable with today's Wordle answer
today_date = datetime.date.today()
answer = get_wordle_answer(today_date)

# Print today's Wordle answer if the script is run directly
if __name__ == "__main__":
    print(f"Today's NYT Wordle answer is '{answer}'")
