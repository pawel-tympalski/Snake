import pygame, time, os
from board import Board


def start_game():
    pygame.init()
    screen_width = 600
    screen_height = 600
    silver = (192, 192, 192)
    board = Board(screen_width, screen_height, silver)

    start_x = 100
    start_y = 100

    score = board.play(start_x, start_y)
    return score


def show_intro():
    screen = pygame.display.set_mode((300, 200))
    current_directory_path = os.getcwd()
    print(os.path.join(current_directory_path, 'snake1.png'))

    surface = pygame.image.load(os.path.join(current_directory_path, 'snake1.png'))
    rect = pygame.Rect((0, 0), (300, 200))

    surface = pygame.transform.scale(surface, rect.size)

    screen.blit(surface, (0, 0))

    pygame.display.flip()
    time.sleep(2)


def show_game_over(score):
    pygame.init()
    size = (400, 200)
    screen = pygame.display.set_mode(size)


    text = "Game over" \
           " your score: " + str(score)

    myfont = pygame.font.SysFont('Fira Code', 30)

    textsurface = myfont.render(text, False, (192, 192, 192))
    screen.blit(textsurface, (0, 0))
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()

if __name__ == "__main__":
    show_intro()
    score = start_game()
    show_game_over(score)