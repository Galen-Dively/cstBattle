import socket
import json

class I:
    def __init__(self):
        self.host, self.port = self.getAddress()

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Sever Socket Has Started")
        self.s.bind((self.host, self.port))
        print(f"Socket Has Binded To {self.port}")  

        self.s.listen(4)
        print("Socket Is Listening")

        # for game
        self.playerCount = 0
        self.players = []



    def getAddress(self):
        ip = input("Server IP: ")
        port = int(input("Server Port"))
        return ip, port

    def run(self):
        while True:
            conn, addr = self.s.accept()

            print(f"{addr} has connected")

            self.getPlayerDicts(conn)

        
            conn.close()

    def getPlayerDicts(self, conn):
        conn.send("getPlayer".encode())

        # after retrivering dicts
        # dicts should contain the player id used by the server

        if self.playerCount >= 1:
            conn.send("Waiting For Players: 1. settings".encode())




    def sendPlayerDicts(self, conn):
        conn.send()

    def addPlayer(self):
        pass



class Server:
    def __init__(self):
        self.host, self.port, self.maxPlayers = self.loadServerSettings()
        self.round_settings = self.loadRoundSettings()
        self.s = socket.socket()
        self.firstConnection = False
        self.amountOfPlayers = 0


    def loadServerSettings(self):
        with open("server_settings") as f:
            data = json.loads(f)
        
            return data["ip"], data["port"], data["maxPlayers"]
            

    def loadRoundSettings(self):
        with open("round_settings") as f:
            data = json.loads(f)

            for gamemode in data:
                if gamemode:
                    return gamemode

    def create(self):
        print("Trying to bind")
        self.s.bind((self.host, self.port))
        print("Server Binded")
        self.s.listen(self.maxPlayers)
        self.menu()

    def menu(self):
        i = input(f"1. Start Game 2. Update Menu  [{self.amountOfPlayers}/{self.maxPlayers}]")
        if i == "1" and self.maxPlayers//2 + 1 > self.amountOfPlayers:
            print("Not Enough Players")
            self.startGame()

    def startGame(self):
        pass



