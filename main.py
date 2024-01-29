import pygame 
from frontend.constants import WIDTH , HEIGHT  , SQUARE_SIZE
from backend.server import server


screen = pygame.display.set_mode((800 , 800))


class GameDisplay:
    def __init__(self, screen, server):
        self.screen = screen
        self.server = server

    def display_winner(self, winner_color):
        font = pygame.font.Font(None, 90)
        text = font.render(f"{winner_color} Wins!", True, (255, 255, 255))
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        self.screen.blit(text, text_rect)
        pygame.display.flip()
        pygame.time.wait(10000)  # Display for 2 seconds
        # self.server.reset() 


def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    Server = server(screen)
    game_display = GameDisplay(screen, server)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                print('position clicked is ', pos)
                row, col = get_row_col_from_mouse(pos)
                print('by row and col ', row, col)
                Server.select(row, col)

        Server.update()

        winner_color = Server.winner()
        # print('the winner color is ', winner_color)
        if winner_color:
            game_display.display_winner(winner_color)
            running = False

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()


# main()

    