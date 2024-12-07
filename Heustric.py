class HeuristicFunction:
    def __init__(self,k):
        self.hh=k
        
        

    def evaluate_board(self, board):
        """
        Evaluate the board state (heuristic function).
        """
        score = 0
        definsive=1000000*self.check4(board,'X')+100*self.check3(board,'X')+10*self.check2(board,'X')
        aggrisive=100000*self.check4(board,'O')+100*self.check3(board,'O')+10*self.check2(board,'O')
        score=aggrisive-definsive
        return score

    def is_valid(self, x, y, n, m):
        return 0 <= x < n and 0 <= y < m

    def check3(self, board, Player):
        n = len(board)
        m = len(board[0])
        count = 0

        # Check horizontal, vertical, and diagonal directions
        for i in range(n):
            for j in range(m):
                # Horizontal (e.g., _Player, Player_P, etc.)
                if j + 3 < m:
                    if board[i][j] == ' ' and board[i][j+1] == Player and board[i][j+2] == Player and board[i][j+3] == Player:
                        count += 1
                    if board[i][j] == Player and board[i][j+1] == Player and board[i][j+2] == ' ' and board[i][j+3] == Player:
                        count += 1
                    if board[i][j] == Player and board[i][j+1] == ' ' and board[i][j+2] == Player and board[i][j+3] == Player:
                        count += 1
                    if board[i][j] == Player and board[i][j+1] == Player and board[i][j+2] == Player and board[i][j+3] == ' ':
                        count += 1

                # Vertical (e.g., _Player, Player_P, etc.)
                if i + 3 < n:
                    if board[i][j] == ' ' and board[i+1][j] == Player and board[i+2][j] == Player and board[i+3][j] == Player:
                        count += 1
                    if board[i][j] == Player and board[i+1][j] == Player and board[i+2][j] == ' ' and board[i+3][j] == Player:
                        count += 1
                    if board[i][j] == Player and board[i+1][j] == ' ' and board[i+2][j] == Player and board[i+3][j] == Player:
                        count += 1
                    if board[i][j] == Player and board[i+1][j] == Player and board[i+2][j] == Player and board[i+3][j] == ' ':
                        count += 1

                # Diagonal-right (e.g., _Player, Player_P, etc.)
                if self.is_valid(i + 3, j + 3, n, m):
                    if board[i][j] == ' ' and board[i+1][j+1] == Player and board[i+2][j+2] == Player and board[i+3][j+3] == Player:
                        count += 1
                    if board[i][j] == Player and board[i+1][j+1] == Player and board[i+2][j+2] == ' ' and board[i+3][j+3] == Player:
                        count += 1
                    if board[i][j] == Player and board[i+1][j+1] == ' ' and board[i+2][j+2] == Player and board[i+3][j+3] == Player:
                        count += 1
                    if board[i][j] == Player and board[i+1][j+1] == Player and board[i+2][j+2] == Player and board[i+3][j+3] == ' ':
                        count += 1

                # Diagonal-left (e.g., _Player, Player_P, etc.)
                if self.is_valid(i + 3, j - 3, n, m):
                    if board[i][j] == ' ' and board[i+1][j-1] == Player and board[i+2][j-2] == Player and board[i+3][j-3] == Player:
                        count += 1
                    if board[i][j] == Player and board[i+1][j-1] == Player and board[i+2][j-2] == ' ' and board[i+3][j-3] == Player:
                        count += 1
                    if board[i][j] == Player and board[i+1][j-1] == ' ' and board[i+2][j-2] == Player and board[i+3][j-3] == Player:
                        count += 1
                    if board[i][j] == Player and board[i+1][j-1] == Player and board[i+2][j-2] == Player and board[i+3][j-3] == ' ':
                        count += 1

        return count

    def check2(self, board, Player):
        n = len(board)
        m = len(board[0])
        count = 0

        # Check for each possible starting position
        for i in range(n):
            for j in range(m):
                # Check horizontal patterns
                if j + 3 < m:
                    # x_x_
                    if (board[i][j] == Player and board[i][j + 2] == Player and
                        board[i][j + 1] == ' ' and self.is_valid(i, j + 3, n, m) and board[i][j + 3] == ' '):
                        count += 1

                    # x__x
                    if (board[i][j] == Player and board[i][j + 3] == Player and
                        board[i][j + 1] == ' ' and board[i][j + 2] == ' '):
                        count += 1

                    # xx__
                    if (board[i][j] == Player and board[i][j + 1] == Player and
                        board[i][j + 2] == ' ' and board[i][j + 3] == ' '):
                        count += 1

                    # _x_x
                    if (board[i][j + 1] == Player and board[i][j + 3] == Player and
                        board[i][j] == ' ' and board[i][j + 2] == ' '):
                        count += 1

                    # __xx
                    if (board[i][j + 2] == Player and board[i][j + 3] == Player and
                        board[i][j] == ' ' and board[i][j + 1] == ' '):
                        count += 1

                    # _XX_
                    if (board[i][j] == ' ' and board[i][j + 1] == Player and
                        board[i][j + 2] == Player and board[i][j + 3] == ' '):
                        count += 1

                # Check vertical patterns
                if i + 3 < n:
                    # x_x_
                    if (board[i][j] == Player and board[i + 2][j] == Player and
                        board[i + 1][j] == ' ' and self.is_valid(i + 3, j, n, m) and board[i + 3][j] == ' '):
                        count += 1

                    # x__x
                    if (board[i][j] == Player and board[i + 3][j] == Player and
                        board[i + 1][j] == ' ' and board[i + 2][j] == ' '):
                        count += 1

                    # xx__
                    if (board[i][j] == Player and board[i + 1][j] == Player and
                        board[i + 2][j] == ' ' and board[i + 3][j] == ' '):
                        count += 1

                    # _x_x
                    if (board[i + 1][j] == Player and board[i + 3][j] == Player and
                        board[i][j] == ' ' and board[i + 2][j] == ' '):
                        count += 1

                    # __xx
                    if (board[i + 2][j] == Player and board[i + 3][j] == Player and
                        board[i][j] == ' ' and board[i + 1][j] == ' '):
                        count += 1

                    # _XX_
                    if (board[i][j] == ' ' and board[i + 1][j] == Player and
                        board[i + 2][j] == Player and board[i + 3][j] == ' '):
                        count += 1

                if i + 3 < n and j + 3 < m:
                    # Check each pattern for diagonal (bottom-right direction)
                    # x_x_
                    if (board[i][j] == Player and board[i + 2][j + 2] == Player and
                        board[i + 1][j + 1] == ' ' and self.is_valid(i + 3, j + 3, n, m) and board[i + 3][j + 3] == ' '):
                        count += 1

                    # x__x
                    if (board[i][j] == Player and board[i + 3][j + 3] == Player and
                        board[i + 1][j + 1] == ' ' and board[i + 2][j + 2] == ' '):
                        count += 1

                    # xx__
                    if (board[i][j] == Player and board[i + 1][j + 1] == Player and
                        board[i + 2][j + 2] == ' ' and board[i + 3][j + 3] == ' '):
                        count += 1

                    # _x_x
                    if (board[i + 1][j + 1] == Player and board[i + 3][j + 3] == Player and
                        board[i][j] == ' ' and board[i + 2][j + 2] == ' '):
                        count += 1

                    # __xx
                    if (board[i + 2][j + 2] == Player and board[i + 3][j + 3] == Player and
                        board[i][j] == ' ' and board[i + 1][j + 1] == ' '):
                        count += 1

                    # _XX_
                    if (board[i][j] == ' ' and board[i + 1][j + 1] == Player and
                        board[i + 2][j + 2] == Player and board[i + 3][j + 3] == ' '):
                        count += 1

                # Check diagonal-left (/ direction)
                if i + 3 < n and j - 3 >= 0:
                    # Check each pattern for diagonal (bottom-left direction)
                    # x_x_
                    if (board[i][j] == Player and board[i + 2][j - 2] == Player and
                        board[i + 1][j - 1] == ' ' and self.is_valid(i + 3, j - 3, n, m) and board[i + 3][j - 3] == ' '):
                        count += 1

                    # x__x
                    if (board[i][j] == Player and board[i + 3][j - 3] == Player and
                        board[i + 1][j - 1] == ' ' and board[i + 2][j - 2] == ' '):
                        count += 1

                    # xx__
                    if (board[i][j] == Player and board[i + 1][j - 1] == Player and
                        board[i + 2][j - 2] == ' ' and board[i + 3][j - 3] == ' '):
                        count += 1

                    # _x_x
                    if (board[i + 1][j - 1] == Player and board[i + 3][j - 3] == Player and
                        board[i][j] == ' ' and board[i + 2][j - 2] == ' '):
                        count += 1

                    # __xx
                    if (board[i + 2][j - 2] == Player and board[i + 3][j - 3] == Player and
                        board[i][j] == ' ' and board[i + 1][j - 1] == ' '):
                        count += 1

                    # _XX_
                    if (board[i][j] == ' ' and board[i + 1][j - 1] == Player and
                        board[i + 2][j - 2] == Player and board[i + 3][j - 3] == ' '):
                        count += 1
                        # Check diagonal right (\ direction)

                                # Similar patterns for diagonals can be added here

        return count

    def check4(self, board, Player):
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

        return count
