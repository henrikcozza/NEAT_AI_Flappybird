import pygame
from configs import FLOOR_IMAGE


class Floor:
    speed = 5
    width = FLOOR_IMAGE.get_width()
    sprite = FLOOR_IMAGE

    def __init__(self, y):
        self.y = y
        self.x1 = 0
        self.x2 = self.width

    def move(self):
        self.x1 -= self.speed
        self.x2 -= self.speed
        if self.x1 + self.width < 0:
            self.x1 = self.x2 + self.width
        if self.x2 + self.width < 0:
            self.x2 = self.x1 + self.width
        
    def draw(self, screen):
        screen.blit(self.sprite, (self.x1, self.y) )
        screen.blit(self.sprite, (self.x2, self.y) )
