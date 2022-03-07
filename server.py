import socket
import json
import os

class Server:
    def __init__(self):
        self.host, self.port, self.maxPlayers = self.loadServerSettings()
        self.round_settings = self.loadRoundSettings()
        self.s = socket.socket()
        self.firstConnection = False
        self.amountOfPlayers = 0
        self.running = False

        self.players = []



    def loadServerSettings(self):
        path = os.getcwd() + "/" + "network/server_settings.json"
        data = open(path)
        data = json.load(data)
        
        return data["ip"], int(data["port"]), data["maxPlayers"]
            

    def loadRoundSettings(self):
        path = os.getcwd() + "/" + "network/round_settings.json"
        data = open(path)
        data = json.load(data)

        for gamemode in data:
            if gamemode:
                return gamemode

    def create(self):
        print("Trying to bind")
        self.s.bind((self.host, self.port))
        print("Server Binded")
        self.s.listen(self.maxPlayers)
        self.running = True

    def menu(self):
        i = input(f"1. Start Game 2. Update Menu  [{self.amountOfPlayers}/{self.maxPlayers}]")
        if i == "1" and self.maxPlayers//2 + 1 > self.amountOfPlayers:
            print("Not Enough Players")
            self.menu()
        if i == "1":
            self.startGame()
        if i == "2":
            self.menu()

    def startGame(self):
        pass

    def update(self):
        while self.running:
            conn, addr = self.s.accept()
            print(f"{addr} has connected")
            self.amountOfPlayers += 1
            self.getPlayerDicts(conn)
            i = self.sendPlayerDicts(conn)
            self.players.append(i)
            self.exit(conn)


    def exit(self, conn):
        conn.close()


    def sendPlayerDicts(self, conn):
        for player in self.players:
            i = json.dumps(player)
            try:
                conn.send(i).encode()
            except:
                pass

    def getPlayerDicts(self, conn):
        try:
            i = conn.recv(1024).decode()
            print(i)
            return i

        except:
            pass


server = Server()
server.create()
server.update()