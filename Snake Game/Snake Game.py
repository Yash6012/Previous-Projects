import pygame
import random
import os

pygame.mixer.init()
pygame.init()


white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
Screen_Width = 900
Screen_Height = 600

gamewindow = pygame.display.set_mode((Screen_Width, Screen_Height))

Background = pygame.image.load("12.jpg")
Background = pygame.transform.scale(Background, (Screen_Width, Screen_Height)).convert_alpha()



pygame.display.set_caption("First Snake Game")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)


def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gamewindow.blit(screen_text, [x, y])


def plot_snake(gamewindow, color, Snk_list, Snakesize):
    for x, y in Snk_list:
        pygame.draw.rect(gamewindow, color, [x, y, Snakesize, Snakesize])

def welcome():
    exit_game = False
    while not exit_game:
        gamewindow.fill((200, 200, 100))
        text_screen("Welcome To Snakes Game", black, 180, 260)
        text_screen("Press BACKSPACE To Play", black, 180, 290)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    pygame.mixer.music.load("Game.mp3")
                    pygame.mixer.music.play()
                    gameloop()



        pygame.display.update()
        clock.tick(60)



def gameloop():
    # variable
    fps = 60
    exit_game = False
    game_over = False
    Snake_x = 45
    Snake_y = 55
    if (not os.path.exists("Highscore.txt")):
        with open("Highscore.txt", "w")as f:
            f.write("0")
    with open("Highscore.txt", "r")as f:
        Highscore = f.read()
    f_x = random.randint(20, Screen_Width / 2)
    f_y = random.randint(20, Screen_Height / 2)
    Velocity_x = 0
    Velocity_y = 0
    init_velocity = 5
    Snakesize = 25
    Score = 0
    Snk_list = []
    Snk_length = 1

    while not exit_game:
        if game_over:
            with open("Highscore.txt", "w")as f:
                f.write(str(Highscore))
            gamewindow.fill(white)
            text_screen("Game Over : Press Enter To RESTART", red, 100, 250)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        Velocity_x = init_velocity
                        Velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        Velocity_x = -init_velocity
                        Velocity_y = 0

                    if event.key == pygame.K_UP:
                        Velocity_y = -init_velocity
                        Velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        Velocity_y = init_velocity
                        Velocity_x = 0
            Snake_x = Snake_x + Velocity_x
            Snake_y = Snake_y + Velocity_y

            if abs(Snake_x - f_x) < 20 and abs(Snake_y - f_y) < 20:
                Score += 10
                f_x = random.randint(20, Screen_Width / 2)
                f_y = random.randint(20, Screen_Height / 2)
                Snk_length += 5
                if Score > int(Highscore):
                    Highscore = Score

            gamewindow.fill(white)
            gamewindow.blit(Background, (0, 0))
            text_screen("Score :" + str(Score) + "  High Score:" + str(Highscore), red, 5, 5)
            pygame.draw.rect(gamewindow, red, [f_x, f_y, Snakesize, Snakesize])
            head = []
            head.append(Snake_x)
            head.append(Snake_y)
            Snk_list.append(head)

            if len(Snk_list) > Snk_length:
                del Snk_list[0]

            if head in Snk_list[:-1]:
                game_over = True
                pygame.mixer.music.load("Game Over.mp3")
                pygame.mixer.music.play()

            if Snake_x < 0 or Snake_x > Screen_Width or Snake_y < 0 or Snake_y > Screen_Height:
                game_over = True
                pygame.mixer.music.load("Game Over.mp3")
                pygame.mixer.music.play()
            plot_snake(gamewindow, black, Snk_list, Snakesize)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()


welcome()
