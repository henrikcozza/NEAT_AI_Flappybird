import pygame
from configs import SCREEN_WIDTH, SCREEN_HEIGHT, BACKGROUND_IMAGE, FONT_SCORE
from Bird import Bird
from Pipe import Pipe
from Floor import Floor


def draw_screen(screen, birds, pipes, floor, score):
    screen.blit(BACKGROUND_IMAGE, (0,0) )
    for bird in birds:
        bird.draw(screen)
    for pipe in pipes:
        pipe.draw(screen)
    text_score =  FONT_SCORE.render(f"Score: {score}", 1, (255, 255, 255) )
    screen.blit(text_score, (SCREEN_WIDTH -10 - text_score.get_width(),text_score.get_height() + 20 ) )
    floor.draw(screen)
    pygame.display.update()

def main():
    birds = [Bird(230, 350)]
    floor = Floor(SCREEN_HEIGHT - 70)
    pipes = [Pipe(SCREEN_WIDTH + 200)]
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    score = 0
    timer = pygame.time.Clock()
    while True:
        timer.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    for bird in birds:
                        bird.jump()
        for bird in birds:
            bird.move()
        floor.move()
        add_pipe = False
        removed_pipes = []
        for pipe in pipes:
            for index, bird in enumerate(birds):
                if pipe.is_collided(bird):
                    birds.pop(index)
                if not pipe.overtook_bird and bird.x > pipe.x:
                    pipe.overtook_bird = True
                    add_pipe = True
            pipe.move()
            if pipe.x + pipe.sprite_top.get_width() < 0:
               removed_pipes.append(pipe)
        if add_pipe:
            score += 1
            pipes.append(Pipe(SCREEN_WIDTH))
        for pipe in removed_pipes:
             pipes.remove(pipe)
        
        for index, bird in enumerate(birds):
            if (bird.y + bird.sprite.get_height()) > floor.y or bird.y <= 0:
                birds.pop(index)
        draw_screen(screen, birds, pipes, floor, score)

if __name__ == '__main__':
    main()