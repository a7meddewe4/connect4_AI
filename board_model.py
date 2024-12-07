"""Board state and game logic"""

from constants import PLAYER_SCORE


class BoardModel:
    def __init__(self, rows=6, cols=7):
        self.rows = rows
        self.cols = cols
        self.grid = [[' ' for _ in range(cols)] for _ in range(rows)]
        self.score = {
            'X': 0,
            'O': 0
        }
         

    
        
    def is_valid_move(self, col):
        return 0 <= col < self.cols and self.grid[0][col] == ' '
    
    def get_next_open_row(self, col):
        for row in range(self.rows - 1, -1, -1):
            if self.grid[row][col] == ' ':
                return row
        return -1
    
    def make_move(self, col, player):
        row = self.get_next_open_row(col)
        if row != -1:
            self.grid[row][col] = player
            return True, row
        return False, -1
    
    def update_score2(self, player, ):
        # Check horizontal
        for row in range(self.rows):
            for col in range(self.cols - 3):
                if all(self.grid[row][col + i] == player for i in range(4)):
                    # self.score[player] +=1
                    # print("Score changed to: " + str(self.score[player]))
                    return 
        
        # Check vertical
        for row in range(self.rows - 3):
            for col in range(self.cols):
                if all(self.grid[row + i][col] == player for i in range(4)):
                    # print("Score changed to: " + str(self.score[player]))
                    # self.score[player] +=1 
                    return 
        
        # Check diagonal (positive slope)
        for row in range(self.rows - 3):
            for col in range(self.cols - 3):
                if all(self.grid[row + i][col + i] == player for i in range(4)):
                    # print("Score changed to: " + str(self.score[player]))
                    # self.score[player] +=1 
                    return 
        
        # Check diagonal (negative slope)
        for row in range(3, self.rows):
            for col in range(self.cols - 3):
                if all(self.grid[row - i][col + i] == player for i in range(4)):
                    # print("Score changed to: " + str(self.score[player]))
                    # self.score[player] +=1 
                    return 
        
        return False
    def update_score(self, Player):
        board=self.grid
        n = len(board)
        m = len(board[0])
        count = 0

    # Check horizontal, vertical, and diagonal directions for a pattern of 4.
        for i in range(n):
         for j in range(m):
            # Horizontal (e.g., Player_Player_Player_Player)
            if j + 3 < m:
                if board[i][j] == Player and board[i][j + 1] == Player and board[i][j + 2] == Player and board[i][j + 3] == Player:
                    count += 1

            # Vertical (e.g., Player_Player_Player_Player)
            if i + 3 < n:
                if board[i][j] == Player and board[i + 1][j] == Player and board[i + 2][j] == Player and board[i + 3][j] == Player:
                    count += 1

            # Diagonal-right (\ direction)
            if i + 3 < n and j + 3 < m:
                if board[i][j] == Player and board[i + 1][j + 1] == Player and board[i + 2][j + 2] == Player and board[i + 3][j + 3] == Player:
                    count += 1

            # Diagonal-left (/ direction)
            if i + 3 < n and j - 3 >= 0:
                if board[i][j] == Player and board[i + 1][j - 1] == Player and board[i + 2][j - 2] == Player and board[i + 3][j - 3] == Player:
                    count += 1
        self.score[Player]=count
    def is_full(self):
        return all(self.grid[0][col] != ' ' for col in range(self.cols))
    
    def reset(self):
        self.score = {
            'X': 0,
            'O': 0
        }  # Reset score to 0

        self.grid = [[' ' for _ in range(self.cols)] for _ in range(self.rows)]
    def get_code(self):
        result = []
       
        
        for i in range(7):  
             
            for j in range(6):  
                 result.append(self.grid[j][i])
            
        
        return ''.join(result) ;      
    def unmake_move(self, row,col):
        
        
            self.grid[row][col] = ' '
        