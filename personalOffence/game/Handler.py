
class Handler:
    def __init__(self):
        # stores all game objects in level
        self.game_objects = []

    # adds an object to game objects list
    def addObject(self, object):
        self.game_objects.append(object)

    def removeObject(self, object):
        self.game_objects.remove(object)
    
    def tick(self):
        for game_object in self.game_objects:
            game_object.tick()
            try:
                game_object.move()
            except:
                pass
        
    def render(self, screen):
        for game_object in self.game_objects:
            game_object.render(screen)