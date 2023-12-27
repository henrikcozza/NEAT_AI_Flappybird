import os
import pygame
from configs import SCREEN_WIDTH, SCREEN_HEIGHT, BACKGROUND_IMAGE, FONT_SCORE, AI_IS_PLAY, GENERATION, BEST_SCORE
from sprites import Bird, Floor, Pipe
import neat 


def draw_screen(screen, birds, pipes, floor, score = 0, generation = 0):
    global BEST_SCORE
    screen.blit(BACKGROUND_IMAGE, (0,0) )
    for bird in birds:
        bird['instance'].draw(screen)
    for pipe in pipes:
        pipe.draw(screen)
    text_score =  FONT_SCORE.render(f"Score: {score}", 1, (255, 255, 255) )
    screen.blit(text_score, (SCREEN_WIDTH -10 - text_score.get_width(),text_score.get_height() + 20 ) )
    if AI_IS_PLAY:
        text_generation =  FONT_SCORE.render(f"Generation: {GENERATION}", 1, (255, 255, 255) )
        screen.blit(text_generation, (10,text_generation.get_height() + 5 ) )        
    if score > BEST_SCORE:
        BEST_SCORE = score
    text_generation =  FONT_SCORE.render(f"Best score: {BEST_SCORE}", 1, (255, 255, 255) )
    screen.blit(text_generation, (10,text_generation.get_height() + 40 ) )

    floor.draw(screen)
    pygame.display.update()

def main(genomes, config): #fitness function
    global GENERATION
    GENERATION += 1

    if AI_IS_PLAY:
        birds = []
        for _, genome in genomes:
            bird = {}
            bird['network'] = neat.nn.FeedForwardNetwork.create(genome, config)
            # this is a value to reward or punishment
            genome.fitness = 0
            bird['genome'] = genome
            bird['instance'] = Bird(230, 350)
            birds.append(bird)
    else:
        birds = [
            {
                'instance': Bird(230, 350),
                'network': None,
                'genome': None
             
             }]
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
            if event.type == pygame.KEYDOWN and not AI_IS_PLAY:
                if event.key == pygame.K_SPACE:
                    for bird in birds:
                        bird['instance'].jump()
        pipe_index = 0
        if len(birds) > 0:
            if len(pipes) > 1 and birds[0]['instance'].x > pipes[0].sprite_top.get_width():
                pipe_index = 1
        else:
            break
        # move things
        for index, bird in enumerate(birds):
                bird['instance'].move()
                if AI_IS_PLAY:
                    # incrase a litle bit the fitness of bird
                    inputs = (
                        bird['instance'].y,
                        abs(bird['instance'].y - pipes[pipe_index].height),
                        abs(bird['instance'].y - pipes[pipe_index].position_down),                  
                    )
                    bird['genome'].fitness += 0.1
                    neural_output = bird['network'].activate(inputs)
                    if neural_output[0] > 0.5:
                        bird['instance'].jump()
        floor.move()
        add_pipe = False
        removed_pipes = []
        for pipe in pipes:
            for index, bird in enumerate(birds):
                if pipe.is_collided(bird['instance']):
                    if AI_IS_PLAY:
                        bird['genome'].fitness -= 1
                    birds.pop(index)
                if not pipe.overtook_bird and bird['instance'].x > pipe.x:
                    pipe.overtook_bird = True
                    add_pipe = True
            pipe.move()
            if pipe.x + pipe.sprite_top.get_width() < 0:
               removed_pipes.append(pipe)
        if add_pipe:
            score += 1
            
            pipes.append(Pipe(SCREEN_WIDTH))
            if AI_IS_PLAY:
                for bird in birds:
                    bird['genome'].fitness += 5
        for pipe in removed_pipes:
             pipes.remove(pipe)        
        for index, bird in enumerate(birds):
            if (bird['instance'].y + bird['instance'].sprite.get_height()) > floor.y or bird['instance'].y <= 0:
                birds.pop(index)
        draw_screen(screen, birds, pipes, floor, score)

def run(path_config):
    config = neat.config.Config(neat.DefaultGenome,
                                neat.DefaultReproduction,
                                neat.DefaultSpeciesSet,
                                neat.DefaultStagnation,
                                path_config)
    if AI_IS_PLAY:
        bird_population = neat.Population(config)
        bird_population.add_reporter(neat.StdOutReporter(True))
        bird_population.add_reporter(neat.StatisticsReporter())
        bird_population.run(main, 50)
    else:
        main(None, None)

if __name__ == '__main__':
    path = os.path.dirname(__file__)
    path_config = os.path.join(path, 'neat_setup.txt')
    run(path_config)
    