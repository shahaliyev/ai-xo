import json
import requests


# Creates game and returns gameId
def createGame(userId, teamId1, teamId2, boardSize, target):
    
    url = "https://www.notexponential.com/aip2pgaming/api/index.php"
    
    headers = {
        'x-api-key': 'e7e036090926b66d6888',
        'userId': userId,
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'  
    }
    
    payload = {
        'type': 'game',
        'teamId1': teamId1,
        'teamId2': teamId2,
        'gameType': 'TTT',
        'boardSize': boardSize,
        'target': target
    }
    
    response = requests.post(url, headers=headers, data=payload)
    print(response.text)
    parsed = json.loads(response.text)
    return parsed['gameId']


def getMyGames(userId, whichGames):
    
    url = "https://www.notexponential.com/aip2pgaming/api/index.php?type=" + whichGames
    
    headers = {
        'x-api-key': 'e7e036090926b66d6888',
        'userId': userId,
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'  
    }
    
    response = requests.get(url, headers=headers)
    
    print(response.text)


# Makes move and returns moveId
def makeMove(userId, gameId, teamId1, move):
    
    url = "https://www.notexponential.com/aip2pgaming/api/index.php"
    
    headers = {
        'x-api-key': 'e7e036090926b66d6888',
        'userId': userId,
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'  
    }
    
    payload = {
        'type': 'move',
        'gameId': gameId,
        'teamId': teamId1,
        'move': move
    }
    
    response = requests.post(url, headers=headers, data=payload)
    print(response.text)
    parsed = json.loads(response.text)
    return parsed['code'], parsed['moveId']


# Gets moves and return lastMove
def getMoves(gameId, count):
    
    url = "https://www.notexponential.com/aip2pgaming/api/index.php?type=moves&gameId=" + gameId + "&count=" + count
    
    headers = {
        'x-api-key': 'e7e036090926b66d6888',
        'userId': userId,
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'  
    }
    
    response = requests.get(url, headers=headers)
    print(response.text)
    parsed = json.loads(response.text)
    return parsed['moves'][0]['symbol'], parsed['moves'][0]['move']


# boardMap = 1 for Board Map, 0 for Board String
def getBoard(boardMap, gameId):
    
    if boardMap == 0:
        url = "https://www.notexponential.com/aip2pgaming/api/index.php?type=boardString&gameId=" + gameId
    if boardMap == 1:
        url = "https://www.notexponential.com/aip2pgaming/api/index.php?type=boardMap&gameId=" + gameId
    
    headers = {
        'x-api-key': 'e7e036090926b66d6888',
        'userId': userId,
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'  
    }
    
    response = requests.get(url, headers=headers)
    
    print(response.text)


# Examples
userId = "1039"
teamId1 = "1251"
teamId2 = "1263"
boardSize = "3"
target = "3"
whichGames = "myOpenGames"
count = "1"

gameId = str(createGame(userId, teamId1, teamId2, boardSize, target))

getMyGames(userId, whichGames)

moveId = str(makeMove(userId, gameId, teamId1, "1,1"))

lastMove = getMoves(gameId, count)

getBoard(0, gameId)

getBoard(1, gameId)
