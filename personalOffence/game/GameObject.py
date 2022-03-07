from abc import abstractmethod
# base object for everything in game, used mostly as parent for other types of objects, such as ui and physics objects

class GameObject:
    def __init__(self, id, layer):
        # assings attrs
        self.id = id
        self.layer = layer

    @abstractmethod
    def tick(self):
        pass

    @abstractmethod
    def render(self, screen):
        pass
