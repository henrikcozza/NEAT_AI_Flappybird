# configs.py
import pygame
import os
import random


# screen configurations
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 800
PIPE_IMAGE = pygame.transform.scale2x(
    pygame.image.load(
        os.path.join("assets","images","pipe.png")
    )
)
FLOOR_IMAGE = pygame.transform.scale2x(
    pygame.image.load(
        os.path.join("assets","images","base.png")
    )
)
BACKGROUND_IMAGE = pygame.transform.scale2x(
    pygame.image.load(
        os.path.join("assets","images","bg.png")
    )
)
BIRD_IMAGES = [
    pygame.transform.scale2x(
        pygame.image.load(
            os.path.join("assets","images","bird1.png")
        )
    ),
    pygame.transform.scale2x(
        pygame.image.load(
            os.path.join("assets","images","bird2.png")
        )
    ),
    pygame.transform.scale2x(
        pygame.image.load(
            os.path.join("assets","images","bird3.png")
        )
    ),
]
pygame.font.init()
#TODO change to use project local font 
FONT_SCORE = pygame.font.SysFont('Vineta BT', 50)

# AI configurations
AI_IS_PLAY = True
GENERATION = 0
BEST_SCORE = 0

