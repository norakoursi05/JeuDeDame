import pygame 
from frontend.constants import SILVER , BLACK , ROWS , COLS , SQUARE_SIZE , WHITE,blackPion , WhitePion , GREY
from frontend.pion import Pion

class Plateau :
    def __init__(self):
        self.plateau = []
        self.black_restant = self.white_restant = 12
        self.red_kings = self.white_kings = 0
        self.create_Plateau()

    # Draw just squares 

    def draw_squares(self , win):
        win.fill(SILVER)
        for row in range(ROWS):
            for col in range(row % 2 , COLS , 2):
                pygame.draw.rect(win , BLACK , (row*SQUARE_SIZE , col*SQUARE_SIZE , SQUARE_SIZE , SQUARE_SIZE ))


        
    #  draw just pieces 
            
    def create_Plateau(self):
        for row in range(ROWS):
            self.plateau.append([])
            for col in range(COLS):
                if col % 2 == (( row + 1 ) % 2 ) :
                    if row < 3 :
                        self.plateau[row].append(Pion(row , col , WhitePion))
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


    
    def get_pion(self, row, col):
        return self.plateau[row][col]
    
    def get_pion_color(self , row , col):
        pion = self.get_pion(row, col)
        pion_color = pion.color
        return pion_color 
    

    def changerPosition(self, piece, row, col):
        self.plateau[piece.row][piece.col], self.plateau[row][col] = self.plateau[row][col], self.plateau[piece.row][piece.col]
        piece.move(row, col)

        if row == 7 or row == 0:
            piece.make_king()
            if piece.color == WHITE:
                # piece.color = GREY
                self.white_kings += 1
            else:
                self.red_kings += 1 

    def supprimer (self  , pion):  
        for p in pion: 
            self.plateau[p.row][p.col] = 0 
            print('la couleur de pion skipped from plateau ' , p.color)
            if p.color == WHITE:
                self.white_restant =  self.white_restant-1
                print('the number now of white_restant is' , self.white_restant)
            if p.color == BLACK:
                self.black_restant =  self.black_restant-1
                print('the number now of black_restant is' , self.black_restant)
            

    def winner(self):
        if self.black_restant == 0:
            return WHITE
        elif self.white_restant == 0:
            return BLACK
        return None 

    



        