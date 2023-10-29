import pygame
import random
pygame.init()

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 250)

# Creating window
screen_width = 1200
screen_height = 600
gamewindow = pygame.display.set_mode((screen_width, screen_height))

# Game Title
pygame.display.set_caption("Zarif's Snake")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont("freesans", 25)


def plot_snake(gamewindow, colour, snake_list, snake_size):
    for snake_x, snake_y in snake_list:
        pygame.draw.rect(gamewindow, colour, [snake_x, snake_y, snake_size, snake_size])


def text_screen(text, color, x, y):
    score_screen = font.render(text, True, color)
    gamewindow.blit(score_screen, [x, y])


def gameloop():
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    snake_size = 10
    snake_speed = 3
    velocity_x = 0
    velocity_y = 0
    food_x = random.randint(0, (screen_width-50))
    food_y = random.randint(0, (screen_height-50))
    food_size = 8
    fps = 60
    eating_distance = 6
    eaten = 0

    snake_list = []
    snake_length = 5

    while not exit_game:
        if game_over:
            gamewindow.fill(white)
            text_screen("Game Over!", red, 530, 200)
            text_screen('Press Enter to Continue', blue, 480, 250)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()

        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = snake_speed
                        velocity_y = 0
                    if event.key == pygame.K_LEFT:
                        velocity_x = -snake_speed
                        velocity_y = 0
                    if event.key == pygame.K_UP:
                        velocity_x = 0
                        velocity_y = snake_speed
                    if event.key == pygame.K_DOWN:
                        velocity_x = 0
                        velocity_y = -snake_speed

            snake_x += velocity_x
            snake_y -= velocity_y

            if abs(snake_x-food_x) < eating_distance and abs(snake_y-food_y) < eating_distance:
                food_x = random.randint(10, screen_width-10)
                food_y = random.randint(10, screen_height-10)
                eaten += 5
                score = int(eaten*snake_speed)
                snake_length += 5

            gamewindow.fill(white)
            text_screen('Score:' + str(eaten*snake_speed), red, 5, 5)
            pygame.draw.rect(gamewindow, blue, [food_x, food_y, food_size, food_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            if len(snake_list) > snake_length:
                del snake_list[0]

            if head in snake_list[:-5]:
                game_over = True

            if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
                game_over = True

            plot_snake(gamewindow, red, snake_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
gameloop()

