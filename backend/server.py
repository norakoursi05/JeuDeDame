import pygame 
from frontend.constants import BLACK , WHITE , BLUE , SQUARE_SIZE
from frontend.plateau import Plateau
from frontend.pion import Pion

class server :
    def __init__(self,win ):
        self.selected = None 
        self.plateau = Plateau()
        self.turn = None
        self.valid_moves = {}
        self.win = win 
        self.first = True
    
    def setfirst (self , att):
        self.first = att

    def setTurn(self , turn ):
        self.turn = turn


    
    def update(self):
        self.plateau.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    # # 1 underscore mean private
    def _initialization(self):
        self.selected = None 
        self.plateau = Plateau()
        self.turn = None 
        self.valid_moves = {}

    def reset(self):
        self._initialization()

    def select(self , row , col ):
        if self.selected  :
            # print('we enter here')
            result = self._move(row , col)
            if not result :
                self.selected = None
                self.select(row , col)
        else :
            pion = self.plateau.get_pion(row, col)
            if self.first :
                self.setTurn(pion.color)
                self.first = False
            # print('turn color is ', self.turn)
            if pion != 0 and pion.color == self.turn:
                self.selected = pion
                # print('le pion est :',pion)
                self.valid_moves = self.plateau.get_valid_moves(pion)
                print('valid moves are ', self.valid_moves)
                return True   
            return False
        
  

    # def _move(self, row, col):
    #     piece = self.plateau.get_pion(row, col)
    #     print('the value of the piece is ', piece)

    #     if self.selected and piece == 0 and (row, col) in self.valid_moves:
    #         self.plateau.changerPosition(self.selected, row, col)
    #         skipped = self.valid_moves[(row , col)]
    #         print('the self.first is now ', self.first)
    #         if skipped :
    #             self.plateau.supprimer(skipped)
    #             # print('skipped color :', skipped)
    #             # self.plateau.black_restant =  self.plateau.black_restant-1
    #         self.change_turn()
    #     else:
    #         return False

    #     return True
        
    def _move(self, row, col):
        piece = self.plateau.get_pion(row, col)
        print('the value of the piece is ', piece)

        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            move_info = self.valid_moves[(row, col)]
            # moved_pawn, row , col , color , is_skip = move_info
            if len(move_info) == 4:
                moved_pawn, r, c, is_skip = move_info
                color = None  # or assign a default value if needed
            else:
                moved_pawn, r, c, color, is_skip = move_info

            print('moved_pawn', moved_pawn)
            self.plateau.changerPosition(self.selected, row, col)
            
            if is_skip:
                self.plateau.supprimer(r , c , color)

            self.change_turn()
            print('Move successful!')
        else:
            print('Invalid move!')
            return False

        return True



    
    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, BLUE, (col * SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2), 15)

    def change_turn(self):
        self.valid_moves = {}
        if self.turn == WHITE:
            self.turn = BLACK
        else:
            self.turn = WHITE

    def winner(self):
        return self.plateau.winner()
    

    




    