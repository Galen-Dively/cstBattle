import socket
import json

class Client:
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