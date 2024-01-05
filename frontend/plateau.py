import pygame 
from constants import BLACK , RED , ROWS , COLS , SQUARE_SIZE , WHITE,blackPion , grayPion
from pion import Pion

class Plateau :
    def __init__(self):
        self.plateau = []
        self.red_left = self.white_left = 12
        self.red_kings = self.white_kings = 0
        self.create_Plateau()

    # Draw just squares 

    def draw_squares(self , win):
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(row % 2 , COLS , 2):
                pygame.draw.rect(win , RED , (row*SQUARE_SIZE , col*SQUARE_SIZE , SQUARE_SIZE , SQUARE_SIZE ))


        
    #  draw just pieces 
            
    def create_Plateau(self):
        for row in range(ROWS):
            self.plateau.append([])
            for col in range(COLS):
                if col % 2 == (( row + 1 ) % 2 ) :
                    if row < 3 :
                        self.plateau[row].append(Pion(row , col , grayPion))
                    elif row > 4 :
                        self.plateau[row].append(Pion(row , col , blackPion))
                    else :
                        self.plateau[row].append(0)
                else :
                    self.plateau[row].append(0)
    


    # draw all the squares and pieces 

    def draw(self , win):
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                pion = self.plateau[row][col]
                if pion != 0:
                    pion.draw(win)


        
