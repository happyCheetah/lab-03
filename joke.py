import requests
from typing import Dict

URL = "https://official-joke-api.appspot.com/random_joke"

def get_joke():
    res = requests.get(URL)
    return res.json()

def main():
    temp = get_joke()
    print(temp["setup"])
    print(temp["punchline"])
if __name__ == "__main__":
    main()
    
