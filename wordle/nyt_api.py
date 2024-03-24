import datetime
import requests

date = datetime.date.today()
url = f"https://www.nytimes.com/svc/wordle/v2/{date:%Y-%m-%d}.json"
response = requests.get(url).json()
answer = response["solution"]

if __name__ == "__name__":
    print(f"Today's NYT Wordle answer is '{answer}'")