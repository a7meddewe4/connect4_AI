import math
from Heustric import HeuristicFunction
from LRUcache import LRUCache
class MinMax:
    """
    Minimax implementation for a game, supporting the given board representation with X and O players.
    """
    def __init__(self, depth, is_maximizing):
        self.my_array = [3, 2, 4, 5, 1, 6,0]

        self.probs=[0.6,0.4]
        self.counter=0
        self.depth = depth
        self.is_maximizing = is_maximizing
        self.cache=LRUCache(1000000000)
        self.H=HeuristicFunction(2)

    def minimax(self, depth, is_maximizing,board):
        if self.cache.contains((board.get_code(),depth)): 
            return self.cache.get((board.get_code(),depth))
        """
        Minimax algorithm without pruning.
        """
        if depth == 0 or  board.is_full():
            return self.H.evaluate_board(board.grid),None

        if is_maximizing:
            best_val = -math.inf
            best_move = None
            for i in self.my_array:
                success, row = board.make_move(i, "O")
                if success:
                    val,_= self.minimax(depth - 1, False,board)
                    board.unmake_move(row,i)
                    # best_val = max(best_val, val)
                    print(f"i=${i}   val=${val}   depth =${depth}")
                    if val > best_val:
                        best_val=val
                        best_move = i
            self.cache.insert((board.get_code(),depth),(best_val,best_move))            
            return best_val,best_move
        else:
            best_val = math.inf
            best_move=None
            for i in self.my_array :
                success, row = board.make_move(i, "X")
                if success:
                    val ,_= self.minimax(depth - 1, True,board)
                    
                    board.unmake_move(row,i)
                    print(f"i=${i}   val=${val}   depth =${depth}")
                    if val < best_val:
                        best_val=val
                        best_move = i
            self.cache.insert((board.get_code(),depth),(best_val,best_move))            
            return best_val,best_move


    def minimax_pruning(self, board, depth, alpha, beta, is_maximizing):
        if self.cache.contains((board.get_code(),depth)): 
            return self.cache.get((board.get_code(),depth))
        """
        Minimax algorithm without pruning.
        """
        if depth == 0 or board.is_full() :
            return self.H.evaluate_board(board.grid),None

        if is_maximizing:
            best_val = -math.inf
            best_move=None
            for i in self.my_array:
                success, row = board.make_move(i, "O")
                if success:
                    val,_= self.minimax(depth - 1, False,board)
                    board.unmake_move(row,i)
                    # best_val = max(best_val, val)
                    if val > best_val:
                        best_val=val
                        best_move = i
                    alpha = max(alpha, val)
                    print(f"i=${i}   val=${val}   depth =${depth}")
                    if beta <= alpha:
                        break    
            self.cache.insert((board.get_code(),depth),(best_val,best_move))            
            return best_val,best_move
        else:
            best_val = math.inf
            best_move=None
            for i in self.my_array :
                success, row = board.make_move(i, "X")
                if success:
                    val ,_= self.minimax(depth - 1, True,board)
                    
                    board.unmake_move(row,i)
                    if val < best_val:
                        best_val=val
                        best_move = i
                    beta = min(beta, val)
                    print(f"i=${i}   val=${val}   depth =${depth}")
                    if beta <= alpha:
                        break    
            self.cache.insert((board.get_code(),depth),(best_val,best_move))            
            return best_val,best_move

    
    
    def expect_minimax(self, depth, is_maximizing,chance_node,board,arr):
     
        if depth == 0 :
            return self.H.evaluate_board(board.grid),None
        if chance_node:
                ans=0
                arr2=[[3,2,4,5,1],[0,6]]
                for i in range (2):
                    val,_= self.expect_minimax(depth - 1, is_maximizing,False,board,arr2[i])
                    ans+=val*self.probs[i]
                print(f"chance node   val=${ans}   depth =${depth}")    
                return ans,_             
        else :

            if is_maximizing:
                best_val = -math.inf
                best_move=None
                for i in arr:
                    success, row = board.make_move(i, "O")
                    if success:
                        val,_= self.expect_minimax(depth - 1, False,True,board,arr)
                        board.unmake_move(row,i)
                        print(f"i=${i}   val=${val}   depth =${depth}")
                        if val > best_val:
                            best_val=val
                            best_move = i
                          
                return best_val,best_move
            else:
                best_val = math.inf
                best_move=None
                for i in arr :
                    success, row = board.make_move(i, "X")
                    if success:
                        val,_= self.expect_minimax(depth - 1, True,True,board,arr)
                        print(f"i=${i}   val=${val}   depth =${depth}")
                        board.unmake_move(row,i)
                        if val < best_val:
                            best_val=val
                            best_move = i
                           
            return best_val,best_move
