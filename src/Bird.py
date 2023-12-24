import pygame
from configs import BIRD_IMAGES


class Bird:
    sprites = BIRD_IMAGES
    # rotate animations
    max_rotation = 25
    rotate_speed = 20
    animation_time = 5

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = 0
        self.speed = 0
        self.height = self.y
        self.time = 0
        self.current_sprite = 0
        self.sprite = self.sprites[0]

    def jump(self):
        self.speed =  -8.5
        self.time = 0
        self.height = self.y

    def move(self):
        # calculating
        self.time += 1
        dislocate = 1.5 * (self.time**2) + self.speed * self.time
        # limiting and dislocating
        if dislocate > 16:
            dislocate = 16
        elif dislocate < 0:
            dislocate -=2
        self.y += dislocate
        # angle
        if dislocate < 0 or self.y < (self.height + 50):
            if self.angle < self.max_rotation:
                self.angle = self.max_rotation
            else:
                if self.angle > -90:
                    self.angle -= self.rotate_speed
    
    def draw(self, screen):
        # choice a sprite to use in animation
        self.current_sprite += 1
        if self.current_sprite < self.animation_time:
            self.sprite = self.sprites[0]
        elif self.current_sprite < self.animation_time * 2:
            self.sprite = self.sprites[1]
        elif self.current_sprite < self.animation_time * 3:
            self.sprite = self.sprites[2]
        elif self.current_sprite < self.animation_time * 4:
            self.sprite = self.sprites[1]
        elif self.current_sprite >= (self.animation_time * 4) + 1:
            self.sprite = self.sprites[0]  
            self.current_sprite = 0        
        # if bird go to down dont animate fly
        if self.angle <= -80:
            self.sprite = self.sprites[1]
            self.current_sprite = self.animation_time * 2
        # draw sprite
        rotated_sprite = pygame.transform.rotate(self.sprite, self.angle)
        pivot_sprite = self.sprite.get_rect(topleft=(self.x, self.y)).center
        sprite = rotated_sprite.get_rect(center=pivot_sprite)
        screen.blit(rotated_sprite, sprite.topleft)
    
    def get_mask(self):
        """Returns a mask of the sprite that is used 
        to calculate the collision using perfect pixel precision"""
        return pygame.mask.from_surface(self.sprite)