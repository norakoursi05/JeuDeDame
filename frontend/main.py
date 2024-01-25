import pygame 
from constants import WIDTH , HEIGHT 
from plateau import Plateau


FPS = 60


WIN = pygame.display.set_mode((WIDTH , HEIGHT))

def main():
    run = True 
    clock = pygame.time.Clock()

    plateau = Plateau()

    while run:
        clock.tick(FPS)
        for event in  pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN :
                pos = pygame.mouse.get_pos()
        
        plateau.draw(WIN)
        pygame.display.update()

    pygame.quit()

main()