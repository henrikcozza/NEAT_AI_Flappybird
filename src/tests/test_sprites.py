import pygame
from sprites.Bird import Bird
from sprites.Pipe import Pipe
from sprites.Floor import Floor


# Bird
def test_bird_jump():
    bird = Bird(230, 350)
    bird.jump()    
    bird.move()      
    assert bird.y < 350

def test_bird_has_gravity():
    bird = Bird(230, 350)        
    bird.move()      
    assert bird.y > 350

def test_bird_return_mask():
    bird = Bird(230, 350)
    assert type( bird.get_mask() ) == pygame.mask.Mask

# Floor    
def test_floor_move():
    floor = Floor(30)
    floor.move()
    assert floor.x1 == -(floor.speed)
    assert floor.x2 < floor.width

# Pipe
def test_pipe_move():
    x = 150
    pipe = Pipe(x)
    pipe.move()    
    assert pipe.x < x 

def test_pip_collided():
    pipe = Pipe(150)
    bird = Bird(160, 30)    
    assert pipe.is_collided(bird) == True
    bird2 = Bird(60, 80)    
    assert pipe.is_collided(bird2) == False

def test_pipe_return_mask():
    pipe = Pipe(150)
    assert type( pipe.get_mask(pipe.sprite_top) ) == pygame.mask.Mask