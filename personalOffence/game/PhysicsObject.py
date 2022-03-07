from .GameObject import GameObject
import pygame
import os

class PhysicsObject(GameObject):
    def __init__(self, id, layer, object_assets, attr={"x": 0, "y": 0, "mass": 1}):
        super().__init__(id, layer)

        # sets positional values
        self.x = attr["x"]
        self.y = attr["y"]

        # sets phyics values
        self.mass = attr["mass"]
        self.xVel = 0
        self.yVel = 0
        self.GRAVITY = 7
        self.jumping = False
        self.isGrounded = False

        # animator values
        self.animation_is_idle = True
        self.animation_is_walking_right = False
        self.animation_is_walking_left = False
        self.animation_idle_tick = 5
        self.animation_walking_tick = 7
        self.animation_idle = object_assets[0][0]
        self.animation_walk_left = object_assets[0][1]
        self.currentImage = self.animation_idle[0]
        self.animation_count = 0

        self.w, self.h = self.currentImage.get_width(), self.currentImage.get_height()

    def tick(self):
        self.x += self.xVel
        self.y += self.yVel
        self.animate()


    def render(self, screen):
        screen.blit(self.currentImage, (self.x, self.y))

    def animate(self):
        if self.animation_count + 1 >= len(self.animation_idle) / self.animation_idle_tick:
            self.animation_count = 0

        if self.animation_is_idle:
            self.currentImage = self.animation_idle[self.animation_count//(len(self.animation_idle) // self.animation_idle_tick)]
        if self.animation_is_walking_left:
            self.currentImage = self.animation_walk_left[self.animation_count//(len(self.animation_walk_left)//self.animation_walking_tick)]
        if self.animation_is_walking_right:
           i = self.animation_walk_left[self.animation_count//(len(self.animation_walk_left)//self.animation_walking_tick)]
           self.currentImage = pygame.transform.flip(i, 90, 0)
        
        self.animation_count += 1





        

