from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:

        row, col = len(board), len(board[0])

        print("check row", row)

        print("check col", col)

        # 1. mark T for the border 
        
        def dfs(r, c):
                
            if (r < 0 or c < 0) or ( r == row or c == col) or board[r][c] != 'O':
                return 

            # print("check r<0", -1 < 0)
            board[r][c] = 'T'
            
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
            # print("Check here r :", r,"c :", c)
            # dfs()

        def printFunction(board):
            for b in board:
                print(" ".join(b))

        # 1.1 top & bottom
        for c in range(col):
            dfs(0, c)
            dfs(row-1,c)
            
        # 1.2 left & right
        for r in range(row):
            dfs(r, 0)
            dfs(r, col-1)

        # 2. convert T -> O & inner O -> X 
        
        for r in range(row):
            for c in range(col):
                if board[r][c] == 'T':
                    board[r][c] = 'O'
                elif board[r][c] == 'O':
                    board[r][c] = 'X'
                    
        printFunction(board)

        """
        Do not return anything, modify board in-place instead.
        """
        
if __name__ == "__main__":  
    
    solution = Solution()
    
    board = [
        ["O", "X", "X", "X", "X"],
        ["X", "O", "O", "O", "X"],
        ["X", "X", "O", "O", "X"],  
        ["X", "O", "X", "X", "O"],
        ["X", "O", "O", "O", "X"]
    ]
    
    solution.solve(board)
    