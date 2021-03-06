import json
import math
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
    parsed = json.loads(response.text)
    for key in parsed['myGames'][-1].keys():
        lastGameId = key
    return lastGameId


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
    if parsed['code'] == "OK":
        return parsed['code'], parsed['moveId']
    if parsed['code'] == "FAIL":
        return parsed['code'], False


# Gets moves and return lastMove
def getMoves(userId, gameId, count):
    
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
    if parsed['code'] == "OK":
        return parsed['moves'][0]['symbol'], parsed['moves'][0]['move']
    if parsed['code'] == "FAIL":
        return False, False


# boardMap = 1 for Board Map, 0 for Board String
def getBoard(userId, boardMap, gameId):
    
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
    parsed = json.loads(response.text)
    x = 0
    for item in parsed['output']:
        if item == '-' or item == 'X' or item == 'O':
            x += 1
    boardSize = int(math.sqrt(x))
    return boardSize, parsed['target']
