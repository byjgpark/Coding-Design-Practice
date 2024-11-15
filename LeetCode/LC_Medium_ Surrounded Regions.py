from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:

        row, col = len(board), len(board[0])

        q = deque([]) 
        vis

        for r in range(row):
            for c in range(col):

                if ( r in range(row) or c in range(col)) and board[r][c] == 'O':
                    
                    print("check (r,c)", (r,c))


        # print("row :", row,"col :", col)

        # def dfs(r,c, visit, previValue):
            

        
        # for r in range(row):
            
        

        """
        Do not return anything, modify board in-place instead.
        """
        