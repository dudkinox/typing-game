import requests

def checkPoint(words, expectedWords):
    wordArray = words.split(" ")
    score = 0
    for i in len(expectedWords):
        if wordArray[i] == expectedWords[i]:
            score += 1
        else:
            print("Wrong word: ", wordArray[i])

    print("SCORE : " + score)

def typing():
    words = input(str("go go typing: "))
    return words()

def selectLevel():
    print("SELECT LEVEL")
    print("1. EASY")
    print("2. MEDIUM")
    print("3. HARD")
    print("4. EXPERT")
    level = input(str(": "))

    if level == 1:
        return 10
    elif level == 2:
        return 20
    elif level == 3:
        return 30
    elif level == 4:
        return 40
    else:
        return 100

def getWords(level):
    response = requests.get("https://api.datamuse.com/words?ml=happy&max=" + level)
    if response.status_code == 200:
        words = [word["word"] for word in response.json()]
        print(" ".join(words))
        checkPoint(typing(), words)
    else:
        print("Failed to fetch words.")

def startGame():
    print("ENTER 1 TO START THE GAME")
    isStart = input(str(": "))

    if isStart == 1:
        level = selectLevel()
        getWords(str(level))
    else:
        print("GAME NOT STARTED", isStart)

startGame()