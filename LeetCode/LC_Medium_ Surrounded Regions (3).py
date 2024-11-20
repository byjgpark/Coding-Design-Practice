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

        dfs print(r,c)
            



        # 1.1 top & bottom
        for c in range(col):
            # dfs(0, c)
            # dfs(col-1,c)
            dfs(col-1,c)

        # 2. convert T -> O & inner O -> X 





        """
        Do not return anything, modify board in-place instead.
        """
        