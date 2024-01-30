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
                # we should call the function here
                pion = self.plateau[row][col]
                if pion != 0:
                    pion.draw(win) 


    def get_valid_moves(self, pion):
        ROWS = 7
        moves = {}
        r = pion.row
        print('the row of pion is ', r)
        col = pion.col
        start_ligne_black = r 
        stop_ligne_black = r - 1
        step_ligne_black = -1
        start_ligne_white = r
        stop_ligne_white = r + 1
        step_ligne_white = 1
        print('la couleur du pion is', pion.color)
        if pion.color == BLACK:
            for row in range(start_ligne_black, stop_ligne_black, step_ligne_black):
                if 0 <= row <= ROWS:
                    posibility_one = self.get_pion(row - 1, col - 1)
                    print('posibility one', posibility_one)
                    posibility_two = self.get_pion(row - 1, col + 1)
                    posibility_three = self.get_pion(row - 2, col - 2)
                    posibility_four = self.get_pion(row - 2, col + 2)
                    if posibility_one == 0: 
                        # this false means is skipped or not
                        moves[(row - 1, col - 1)] = (posibility_one, row-1 , col-1 ,  False)
                    if posibility_two == 0:
                        moves[(row - 1, col + 1)] = (posibility_two, row-1 , col-1 ,  False)

                    if posibility_one and posibility_one != 0 and posibility_one.color == WHITE  and posibility_three == 0 : 
                            moves[(row - 2, col - 2)] = (posibility_three, posibility_one.row , posibility_one.col, posibility_one.color ,  True)
                            print('we inter in this case ')
                    if posibility_two and posibility_two != 0 and posibility_two.color == WHITE  and  posibility_four == 0 : 
                            moves[(row - 2, col + 2)] = (posibility_four, posibility_two.row  , posibility_two.col , posibility_two.color ,  True)
                            print('we inter in this case ')

        if pion.color == WHITE :
            for row in range(start_ligne_white, stop_ligne_white, step_ligne_white):
                if 0 <= row < ROWS:
                    posibility_one = self.get_pion(row + 1, col - 1)
                    print('posibility one', posibility_one)
                    posibility_two = self.get_pion(row + 1, col + 1)
                    posibility_three = self.get_pion(row + 2, col - 2)
                    posibility_four = self.get_pion(row + 2, col + 2)
                    if posibility_one == 0: 
                        moves[(row + 1, col - 1)] = (posibility_one , row + 1 , col - 1 , False)
                    if posibility_two == 0:
                        moves[(row + 1, col + 1)] = (posibility_two , row +1 , col+1 ,  False)
                    
                    if posibility_one and posibility_one != 0 and posibility_one.color == BLACK and posibility_three == 0 :  
                        moves[(row + 2, col - 2)] = (posibility_three , posibility_one.row , posibility_one.col , posibility_one.color ,  True)
                        print('we inter in this case ')

                    if posibility_two and posibility_two != 0 and posibility_two.color == BLACK and posibility_four == 0 :  
                        moves[(row + 2, col + 2)] = (posibility_four , posibility_two.row , posibility_two.col , posibility_two.color ,  True)
                        print('we inter in this case ')
        print('the valid moves form method is ', moves)
        return moves

    
 
    # def get_pion(self, row, col):
    #     return self.plateau[row][col]
    def get_pion(self, row, col):
        if 0 <= row < ROWS and 0 <= col < COLS:
            return self.plateau[row][col]
        else:
            # Handle the case when indices are out of range
            return None
    
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

    def supprimer (self  , row , col , color):
        self.plateau[row][col] = 0 
        print('la couleur de pion skipped from plateau ' , color)
        if color == WHITE:
            self.white_restant =  self.white_restant-1
            print('the number now of white_restant is' , self.white_restant)
        if color == BLACK:
            self.black_restant =  self.black_restant-1
            print('the number now of black_restant is' , self.black_restant)
    

            

    def winner(self):
        if self.black_restant == 0:
            return WHITE
        elif self.white_restant == 0:
            return BLACK
        return None 

    







        