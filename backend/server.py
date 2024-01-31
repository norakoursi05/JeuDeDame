import pygame 
from frontend.constants import BLACK , WHITE , BLUE , SQUARE_SIZE , GREY , SILVER , SILVER_DAME
from frontend.plateau import Plateau
from frontend.pion import Pion

class server :
    def __init__(self,win ):
        self.selected = None 
        self.plateau = Plateau()
        self.turn = None
        self.turnK = GREY
        self.valid_moves = {}
        self.win = win 
        self.first = True
        self.continue_turn = False
    
    def setfirst (self , att):
        self.first = att

    def setTurn(self , turn ):
        self.turn = turn
    
    def setTurnK(self , turnk) :
        self.turnk = turnk


    
    def update(self):
        self.plateau.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    def _initialization(self):
        self.selected = None 
        self.plateau = Plateau()
        self.turn = None 
        self.valid_moves = {}

    def reset(self):
        self._initialization()

  
    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)
        else:
            pion = self.plateau.get_pion(row, col)
            if self.first:
                self.setTurnK(GREY if (isinstance(pion, Pion) and pion.color == SILVER) else SILVER)
                self.setTurn(pion.color) if isinstance(pion, Pion) else None
                self.first = False

            if  isinstance(pion, Pion) and pion != 0 and (pion.color == self.turn or pion.color == self.turnk):
                self.selected = pion
                self.valid_moves = self.plateau.get_valid_moves(pion)
                print('valid moves are ', self.valid_moves)
                return True

        return False


    def _move(self, row, col):
        piece = self.plateau.get_pion(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            move_info = self.valid_moves[(row, col)]
            moved_pawn, r, c, is_skip = move_info[:4] if len(move_info) == 4 else move_info[:5]
            color = None if len(move_info) == 4 else move_info[3]

            self.plateau.changerPosition(self.selected, row, col)
            
            if is_skip:
                self.handle_captures(r, c, color)
                self.selected = self.plateau.get_pion(row, col)  # Update selected to the new position
                additional_moves = self.plateau.get_valid_moves(self.selected)
                additional_capture_moves = {move: details for move, details in additional_moves.items() if details[-1]}

                if additional_capture_moves:
                    print('Additional capture moves available, BLACK retains the turn.')
                    return True
                else:
                    print('No additional capture moves, turn changes.')
            self.change_turn()
            self.selected = None  
            return True
        else:
            print('Invalid move!')
            return False


    def handle_captures(self, r, c, color):
        if isinstance(r, (list, tuple)) and isinstance(c, (list, tuple)):
            for skip_row, skip_col in zip(r, c):
                self.plateau.supprimer(skip_row, skip_col, color)
        else:
            self.plateau.supprimer(r, c, color)


    
    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, BLUE, (col * SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2), 15)




    def change_turn(self):
        if hasattr(self, 'continue_turn') and self.continue_turn:

            self.continue_turn = False
            print("BLACK retains the turn after a capture.")
            return  
        self.valid_moves = {}


        if self.turn == WHITE:
            self.turn = BLACK
            self.turnk = GREY  
        elif self.turn == BLACK:
            self.turn = WHITE
            self.turnk = SILVER_DAME  

        elif self.turnK == GREY:
            self.turnK = SILVER_DAME
            self.turn = WHITE
        elif self.turnK == SILVER_DAME:
            self.turnK = GREY
            self.turn = BLACK

      


    def winner(self):
        return self.plateau.winner()
    

    




    