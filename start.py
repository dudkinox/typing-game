import requests

def getWords():
    response = requests.get("https://api.datamuse.com/words?ml=happy&max=100")
    if response.status_code == 200:
        words = [word["word"] for word in response.json()]
        print(words)
    else:
        print("Failed to fetch words.")

def startGame():
    print("ENTER 1 TO START THE GAME")
    isStart = input(str(":"))

    if isStart == 1:
        print("GAME STARTED", isStart)
        getWords()
    else:
        print("GAME NOT STARTED", isStart)

startGame()