import requests
import time

def selectLevel():
    print("SELECT LEVEL")
    print("1. EASY")
    print("2. MEDIUM")
    print("3. HARD")
    print("4. EXPERT")
    level = input(": ")

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

def processScore(typeByPlayer, words, elapsed_time):
    score = 0
    words_list = words.split(" ")
    typeByPlayer_list = typeByPlayer.split(" ")

    for i in range(len(words_list)):
        check = False
        if i < len(typeByPlayer_list) and words_list[i] == typeByPlayer_list[i]:
            score += 1*234
            check = True
        operator = "=" if check else "!="
        print(words_list[i] + operator + (typeByPlayer_list[i] if i < len(typeByPlayer_list) else "MISSING") + "\n")

    print(f"TIME TAKEN: {elapsed_time:.2f} seconds")
    print(f"SUM SCORE : {score / elapsed_time:.2f}")

def getWords(level):
    response = requests.get("https://random-word-api.herokuapp.com/word?number=" + str(level))
    
    if response.status_code == 200:
        words = " ".join(response.json())
        print(words)

        start_time = time.time()
        typeByPlayer = input()
        end_time = time.time()

        elapsed_time = end_time - start_time
        processScore(typeByPlayer, words, elapsed_time)
    else:
        print("Failed to fetch words.\n==============")

def startGame():
    print("ENTER 1 TO START THE GAME")
    isStart = input(": ")

    if isStart == "1":
        level = selectLevel()
        getWords(level)
    else:
        print("GAME NOT STARTED", isStart)

startGame()
