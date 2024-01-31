import pygame 
from frontend.constants import SILVER , BLACK , ROWS , COLS , SQUARE_SIZE , WHITE,blackPion , WhitePion , GREY , SILVER_DAME
from frontend.pion import Pion

class Plateau :
    def __init__(self):
        self.plateau = []
        self.black_restant = self.white_restant = 12
        self.red_kings = self.white_kings = 0
        self.create_Plateau()


    def draw_squares(self , win):
        win.fill(SILVER)
        for row in range(ROWS):
            for col in range(row % 2 , COLS , 2):
                pygame.draw.rect(win , BLACK , (row*SQUARE_SIZE , col*SQUARE_SIZE , SQUARE_SIZE , SQUARE_SIZE ))


        
            
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
    


    def draw(self , win):
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                pion = self.plateau[row][col]
                if pion != 0:
                    pion.draw(win)

                    

    def get_valid_moves(self, pion):
        ROWS = 7
        moves = {}
        r = pion.row
        COLS = 7
        print('the row of pion is ', r)
        col = pion.col
        start_ligne_black = r 
        stop_ligne_black = r - 1
        step_ligne_black = -1
        start_ligne_white = r
        stop_ligne_white = r + 1
        step_ligne_white = 1
        nbr_pion_should_be_deleted = []
        print('la couleur du pion is', pion.color)


        if pion.color == BLACK:
            print('la valeur de pion.dame is ', pion.dame)
            directions = [(-1, -1), (-1, 1)]  
            for d_row, d_col in directions:
                next_row, next_col = r + d_row, col + d_col
                if 0 <= next_row <= ROWS and 0 <= next_col <= COLS:
                    next_pion = self.get_pion(next_row, next_col)
                    if next_pion == 0:
                        moves[(next_row, next_col)] = (next_pion, next_row, next_col, False)
                    elif next_pion.color == WHITE:
                        jump_row, jump_col = next_row + d_row, next_col + d_col
                        if 0 <= jump_row <= ROWS and 0 <= jump_col <= COLS:
                            jump_pion = self.get_pion(jump_row, jump_col)
                            if jump_pion == 0:
                                moves[(jump_row, jump_col)] = (jump_pion, next_row, next_col, True)
                                print('we inter in this case')


        if pion.color == GREY:
            ROWS = 7
            COLS = 7
            r = pion.row
            col = pion.col

            for direction in [(-1, -1), (-1, 1), (1, -1), (1, 1)] :
                d_row, d_col = direction
                for distance in range(1, 8):  
                    dest_row, dest_col = r + distance * d_row, col + distance * d_col
                    if 0 <= dest_row <= ROWS and 0 <= dest_col <= COLS:
                        current_pion = self.get_pion(dest_row, dest_col)
                        if current_pion == 0:
                            moves[(dest_row, dest_col)] = (current_pion, [dest_row], [dest_col], False)
                        elif  current_pion.color == WHITE:
                            skip_row = current_pion.row
                            skip_col = current_pion.col
                            if 0 <= skip_row <= ROWS and 0 <= skip_col <= COLS:
                                posibility = self.get_pion(skip_row, skip_col)
                                if posibility == 0 :
                                    moves[(skip_row, skip_col)] = (posibility,current_pion.row, current_pion.col, current_pion.color, True)
                        else :
                            break


        if pion.color == WHITE:
            print('la valeur de pion.dame is ', pion.dame)
            directions = [(1, -1), (1, 1)]  
            for d_row, d_col in directions:
                next_row, next_col = r + d_row, col + d_col
                if 0 <= next_row <= ROWS and 0 <= next_col <= COLS:
                    next_pion = self.get_pion(next_row, next_col)
                    if next_pion == 0:
                        moves[(next_row, next_col)] = (next_pion, next_row, next_col, False)
                    elif next_pion.color == BLACK:
                        jump_row, jump_col = next_row + d_row, next_col + d_col
                        if 0 <= jump_row <= ROWS and 0 <= jump_col <= COLS:
                            jump_pion = self.get_pion(jump_row, jump_col)
                            if jump_pion == 0:
                                moves[(jump_row, jump_col)] = (jump_pion, next_row, next_col, True)
                                print('we inter in this case')
    
                

       


        if pion.color == SILVER_DAME:
            ROWS = 7
            COLS = 7
            r = pion.row
            col = pion.col

            for direction in [(-1, -1), (-1, 1), (1, -1), (1, 1)] :
                d_row, d_col = direction
                for distance in range(1, 8):  
                    dest_row, dest_col = r + distance * d_row, col + distance * d_col
                    if 0 <= dest_row <= ROWS and 0 <= dest_col <= COLS:
                        current_pion = self.get_pion(dest_row, dest_col)
                        if current_pion == 0:
                            moves[(dest_row, dest_col)] = (current_pion, [dest_row], [dest_col], False)
                        elif  current_pion.color == WHITE:
                            skip_row = current_pion.row
                            skip_col = current_pion.col
                            if 0 <= skip_row <= ROWS and 0 <= skip_col <= COLS:
                                posibility = self.get_pion(skip_row, skip_col)
                                if posibility == 0 :
                                    moves[(skip_row, skip_col)] = (posibility,current_pion.row, current_pion.col, current_pion.color, True)
                        else :
                            break
        return moves
                

    
 
    def get_pion(self, row, col):
        if 0 <= row < ROWS and 0 <= col < COLS:
            return self.plateau[row][col]
        else:
            return None
    
    def get_pion_color(self , row , col):
        pion = self.get_pion(row, col)
        if pion != 0:
            pion_color = pion.color
            return pion_color
        else:
            return None
    

    def changerPosition(self, piece, row, col):
        if piece.dame:
            direction_row = 1 if row > piece.row else -1
            direction_col = 1 if col > piece.col else -1
            temp_row, temp_col = piece.row, piece.col
            while temp_row != row or temp_col != col:
                temp_row += direction_row
                temp_col += direction_col
                temp_piece = self.get_pion(temp_row, temp_col)
                if temp_piece != 0 and temp_piece.color == WHITE:
                    self.supprimer(temp_row, temp_col, WHITE)

        if abs(row - piece.row) == 2 :
            skipped_row = (row + piece.row) // 2
            skipped_col = (col + piece.col) // 2
            self.supprimer(skipped_row, skipped_col, self.get_pion_color(skipped_row, skipped_col))

        self.plateau[piece.row][piece.col], self.plateau[row][col] = self.plateau[row][col], self.plateau[piece.row][piece.col]
        piece.move(row, col)


        self.plateau[piece.row][piece.col], self.plateau[row][col] = self.plateau[row][col], self.plateau[piece.row][piece.col]
        piece.move(row, col)

        if row == 7 or row == 0:
            piece.make_dame()
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

    





#  