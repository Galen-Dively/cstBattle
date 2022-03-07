import socket
import json

class I:
    def __init__(self):
        self.host = "127.0.0.1"
        self.port = 5555

        self.s = socket.socket()

        self.connected = False

    def connectToServer(self, playerDict):
        self.s.connect((self.host, self.port))
        self.connected = True

        data = json.dumps(playerDict)

        i = self.s.recv(1024).decode()
        print(i)

        while self.connected:
            pass

        self.s.send(data)

        self.s.close()

    def sendPlayerDict(self, playerDict):
        pass

    
    def getPlayersDict(self):
        pass


class Client:
    def __init__(self):
        self.host = "127.0.0.1"
        self.port = 5555

        self.s = socket.socket()

        self.connected = False

    def connect(self):
        self.s.connect((self.host, self.port))
        self.connected = True


    def sendPlayerDicts(self, playerDict):
        player = json.dumps(playerDict)
        self.s.send(player.encode())

    def getPlayerDicts(self):
        # retrieves the player dicts from sever and returns them to client
    
        players = self.s.recv(1028).decode()
        print(players)
        return players
