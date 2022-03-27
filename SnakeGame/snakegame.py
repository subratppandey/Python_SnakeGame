import pygame
import time
import random
pygame.init()
pygame.mixer.init()

width, height = 900, 700 

display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')
clock = pygame.time.Clock()
def display_score(game_score):
    position_x, position_y = (width/2)-55,5
    text = score_font.render("Score: " + str(game_score), True, (213, 50, 80))
    display.blit(text, (position_x, position_y))

snake_block = 10
snake_speed = 15
font_style = pygame.font.SysFont("SEGOI UI", 30)
score_font = pygame.font.SysFont("bahnschrift", 35)

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(display, (0,0,0), [
                         x[0], x[1], snake_block, snake_block])
def message(info, color):
    info = font_style.render(info, True, color)
    display.blit(info, [width / 6, height / 3])


def mainLoop():
    food = pygame.image.load("mango.png").convert()
    food_scale = pygame.transform.scale(food, (25, 25))  # Scaling the image
    food_position_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    food_position_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
    display.blit(food_scale, (food_position_x, food_position_y))
    end = False
    game_close = False
    x1, y1 = 350, 250
    x1_change, y1_change = 0, 0
    snake_List = []
    snake_length = 1

    while not end:
        while game_close == True:
            display.fill((255,255,255))
            message("Game Over. Press P to Continue or Q to Quit", (50, 153, 213))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        end = True
                        game_close = False
                    if event.key == pygame.K_p:
                        mainLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True
            crash_sound = pygame.mixer.Sound("crash-sound-effect.mp3")
            pygame.mixer.Sound.play(crash_sound)
        x1 += x1_change
        y1 += y1_change
        display.fill((255,255,255))
        pygame.draw.rect(display, (50,153,213), [
                         food_position_x, food_position_y, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > snake_length:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head: 
                game_close = True

        display_score(snake_length-1)
        our_snake(snake_block, snake_List)

        pygame.display.update()

        if x1 == food_position_x and y1 == food_position_y:
            food_position_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            food_position_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            snake_length += 1
            sound = pygame.mixer.Sound('Tada-sound.mp3')
            pygame.mixer.Sound.play(sound)

        clock.tick(snake_speed)

    pygame.quit()
    quit()
mainLoop()
