import requests

def selectLevel():
    print("SELECT LEVEL")
    print("1. EASY")
    print("2. MEDIUM")
    print("3. HARD")
    print("4. EXPERT")
    level = input(str(": "))

    if level == "1":
        return 10
    elif level == "2":
        return 20
    elif level == "3":
        return 30
    elif level == "4":
        return 40
    else:
        return 100

def processScore(typeByPlayer, words):
    score = 0
    for i in range(len(typeByPlayer.split(" "))):
        check = False
        if words.split(" ")[i] == typeByPlayer.split(" ")[i]:
            score += 1
            check = True
        operator = "=" if check else "!="
        print(words.split(" ")[i] + operator + typeByPlayer.split(" ")[i]+"\n")

    print("SUM SCORE : " + str(score))

def getWords(level):
    response = requests.get("https://random-word-api.herokuapp.com/word?number=" + level)
    # response = requests.get("https://random-word-api.herokuapp.com/word?number=1")
    if response.status_code == 200:
        words = " ".join(response.json())
        print(words)
        typeByPlayer = input()
        processScore(typeByPlayer, words)
    else:
        print("Failed to fetch words.\n==============")

def startGame():
    print("ENTER 1 TO START THE GAME")
    isStart = input(str(": "))

    if isStart == "1":
        level = selectLevel()
        getWords(str(level))
    else:
        print("GAME NOT STARTED", isStart)

startGame()