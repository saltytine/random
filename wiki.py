import webbrowser
import requests

def open_random_wiki():
    url = "https://en.wikipedia.org/wiki/Special:Random"
    response = requests.get(url)
    print(f"Opening: {response.url}")
    webbrowser.open(response.url)

if __name__ == "__main__":
    open_random_wiki()

