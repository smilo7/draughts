import pygame
from draughts.constants import WIDTH, HEIGHT, WHITE
from draughts.game import Game
#from game import Game
#constants
FPS = 60


#set window size and caption
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Draughts - By Candidate 184513 :)")


def main():
    pygame.init()
    clock = pygame.time.Clock()
    game = Game(WINDOW)

    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()



        game.update()
    pygame.quit()


main() #call the main loop
