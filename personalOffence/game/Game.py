import pygame
from .Handler import Handler
from .players import BigGuns
from .attrs import assets
from .attrs import id
from .attrs import layer
from network import Client, Server

class Game:
    def __init__(self, window={"w": 800, "h": 800/2+12*9, "caption": "Default Window"}):
        # sets game window attributes
        self.window_width = window["w"]
        self.window_height = window["h"]
        self.window_caption = window["caption"]

        self.assets = assets.loadAssets()

        # creates window
        self.window = pygame.display.set_mode((self.window_width, self.window_height))
        
        # sets window caption
        pygame.display.set_caption(self.window_caption)

        # creates clock for timing
        self.clock = pygame.time.Clock()

        # creates handler object for game objects
        self.handler = Handler()

        # create obejcts
        self.handler.addObject(BigGuns(self.assets[0], attr={"x": 0, "y": 0, "mass": 1, "layer": layer.GAMEPLAY, "id": id.BIG_GUNS}))

        # create client object for server
        self.server_client = Client()
        self.server_client.connectToServer()

        # get other players
        self.server_other_players = []

        # sets if the game is running
        self.game_running = False
        

    def run(self):
        self.game_running = True
        while self.game_running:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_running = False
            self.window.fill((51, 51, 51))
            self.tick()
            self.render()
            pygame.display.update()
        self.end()

    def tick(self):

        self.handler.tick()

    def render(self):
        self.handler.render(self.window)

    def end(self):
        pygame.quit()
        quit()
    
    def connectGame(self):
        pass

