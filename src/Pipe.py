import random
import pygame
from configs import PIPE_IMAGE, SCREEN_HEIGHT


class Pipe:
    distance = 200
    speed = 5

    def __init__(self, x):
        self.x = x
        self.height = 0
        self.position_top = 0
        self.position_down = 0
        self.sprite_top = pygame.transform.flip(PIPE_IMAGE, False, True)
        self.sprite_down = PIPE_IMAGE 
        self.overtook_bird = False
        self.define_height()

    def define_height(self):
        self.height = random.randrange((SCREEN_HEIGHT * 10) / 100, (SCREEN_HEIGHT * 30) / 100 )
        self.position_top = self.height - self.sprite_top.get_height()
        self.position_down = self.height + self.distance

    def move(self):
        self.x -= self.speed

    def draw(self, screen):
        screen.blit(self.sprite_top, (self.x, self.position_top))
        screen.blit(self.sprite_down, (self.x, self.position_down))

    def is_collided(self, body):
        body_mask = body.get_mask()
        top_pipe_mask = self.get_mask(self.sprite_top)
        down_pipe_mask = self.get_mask(self.sprite_down)
        top_distance = (self.x - body.x, self.position_top - round(body.y) )
        down_distance = (self.x - body.x, self.position_down - round(body.y) )
        top_point = body_mask.overlap(top_pipe_mask, top_distance)
        down_point = body_mask.overlap(down_pipe_mask, down_distance)
        if down_point or top_point:
            return True
        else:
            return False        

    def get_mask(self, sprite):
        """Returns a mask of the sprite that is used 
        to calculate the collision using perfect pixel precision"""
        return pygame.mask.from_surface(sprite)