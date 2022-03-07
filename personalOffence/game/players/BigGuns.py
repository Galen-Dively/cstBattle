from game.PhysicsObject import PhysicsObject
import pygame

class BigGuns(PhysicsObject):
    def __init__(self, assets, attr={"x": 0, "y": 0, "mass": 1, "layer": 0, "id": 0}):
        super().__init__(attr["id"], attr["layer"], assets, attr)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.animation_is_idle = True
            self.animation_is_walking_right = False
            self.animation_is_walking_left = False
        if keys[pygame.K_a]:
            self.xVel = -1
            self.animation_is_walking_right = True
            self.animation_is_walking_left = False
            self.animation_is_idle = False
        if keys[pygame.K_d]:
            self.xVel = 1
            self.animation_is_walking_right = False
            self.animation_is_walking_left = True
            self.animation_is_idle = False

    def getPlayerDict(self):
        return {"x": self.x, "y": self.y, "id": self.id, "mass": self.mass, "layer": self.layer}
        