"""Game state and control logic"""

import math
from tkinter import messagebox
from MinMax import MinMax

class GameController:
        def __init__(self,k, board_model, view):
            self.board = board_model
            self.view = view
            self.current_player = 'X'
            self.m=MinMax(k,True)
            
            self.ai_algorithm = "Other"  # Store the selected AI algori
            self.difficulty = "minimax"
            self.k=k
            
            self.visualize=False
            # self.score={'X':0, 'Y':0}
        # def set_algorithm(self, algorithm):
        #     """Set the AI algorithm."""
        #     self.ai_algorithm = algorithm

        def get_algorithm(self):
            """Get the current AI algorithm."""
            return self.ai_algorithm
        def set_algorithm(self, algorithm):
            """Set the AI algorithm."""
            self.ai_algorithm = algorithm
            # Any additional logic for setting the algorithm

        def set_difficulty(self, difficulty):
            """Set the difficulty level."""
            self.difficulty = difficulty
            # Any additional logic for setting the difficulty, such as adjusting AI behavior
            print(f"Difficulty set to: {difficulty}")
        
            
        def handle_click(self, col):
            
            
            if self.board.is_valid_move(col) and self.current_player=="X":
                success, row = self.board.make_move(col, "X")
                if success:
                    self.view.update_cell(row, col, "X")
                    self.board.update_score("X")
                    if self.board.is_full():
                        if(self.board.score['X']>self.board.score['O']):
                                messagebox.showinfo("Game Over", f"Player X wins!")
                        elif( self.board.score['X']<self.board.score['O']):
                                messagebox.showinfo("Game Over", f"Player O wins!")
                        else:
                            messagebox.showinfo("Game Over", "It's a draw!")
                        self.reset_game()
                        return
                    
                    else:
                        if(self.difficulty=="expect"):
                            _,move=self.m.expect_minimax( self.k, True,False,self.board,[3,2,4,5,1,0,6])
                            success, row = self.board.make_move(move, "O")
                            if success:
                                
                                self.view.update_cell(row, move, "O")
                                self.board.update_score("O")
                        elif self.difficulty=="minimax": 
                            _,move=self.m.minimax( self.k, True,self.board)
                            success, row = self.board.make_move(move, "O")
                            if success:
                                
                                self.view.update_cell(row, move, "O")
                                self.board.update_score("O")
                        else: 
                            _,move=self.m.minimax_pruning(self.board, self.k, -math.inf,math.inf , True)
                            success, row = self.board.make_move(move, "O")
                            if success:
                                
                                self.view.update_cell(row, move, "O")
                                self.board.update_score("O")
                             
                        if self.board.is_full():
                            if(self.board.score['X']>self.board.score['O']):
                                    messagebox.showinfo("Game Over", f"Player X wins!")
                            elif( self.board.score['X']<self.board.score['O']):
                                    messagebox.showinfo("Game Over", f"Player O wins!")
                            else:
                                messagebox.showinfo("Game Over", "It's a draw!")
                            self.reset_game()
                            return        
                       
            
            
                        
                # self.view.update_status(self.current_player)
    
        def switch_player(self):
            
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            

        
        def reset_game(self):
            self.board.reset()
            self.current_player = 'X'
            self.view.reset_board()
            self.view.update_status(self.current_player)