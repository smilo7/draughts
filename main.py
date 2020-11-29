import pygame
from draughts.constants import WIDTH, HEIGHT, BLACK, WHITE, SQUARE_SIZE
from draughts.game import Game
#from game import Game
#constants
FPS = 60


#set window size and caption
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Draughts - By Candidate 184513 :)")

def get_square_coords_from_pos(position):
    x, y = position
    row = y//SQUARE_SIZE
    col = x//SQUARE_SIZE
    return row, col

def main():
    pygame.init()
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Comic Sans MS", 30)
    game = Game(WINDOW, font)

    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    #reset the game
                    print("Game reset")
                    game = Game(WINDOW, font)
                if event.key == pygame.K_ESCAPE:
                    print("Thanks for playing :)")
                    running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                row, col = get_square_coords_from_pos(position)
                game.click(row, col)



        game.update()
    pygame.quit()


main() #call the main loop
