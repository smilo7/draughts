import pygame

#constants
FPS = 60


#set window size and caption
pygame.display.set_mode((800,800))
pygame.display.set_caption("Draughts - By Candidate 184513 :)")


def main():
    pygame.init()
    clock = pygame.time.Clock()


    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()


main() #call the main loop
