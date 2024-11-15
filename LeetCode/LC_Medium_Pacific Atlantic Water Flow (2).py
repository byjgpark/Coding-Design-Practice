class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        row, col = len(heights), len(heights[0])

        print("check row :", row, "column :", col)

        pac, atl = set(), set()

        def dfs(r, c, visit, previValue):

            if (r < 0 or c< 0) or ( (r,c) in visit) or ( r not in range(row) or c not in range(col)) or ( heights[r][c] < previValue):
                return
            
            print("check (r,c)", (r,c))

            visit.add((r,c))

            dfs(r+1, c, visit, heights[r][c])
            dfs(r-1, c, visit, heights[r][c])
            dfs(r, c+1, visit, heights[r][c])
            dfs(r, c-1, visit, heights[r][c])

        # column
        for c in range(col):

            # print("check c", c)

            dfs(0, c, pac, heights[0][c])
            dfs(row-1,c, atl, heights[row-1][c])
        
        # row
        for r in range(row):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, col-1, atl, heights[r][col-1])

        # print("check pac", pac)
        # print("check atl", atl)

        res = []

        for r in range(row):
            for c in range(col):
                if ((r,c) in atl) and ((r,c) in pac):
                    res.append([r,c])

        return res
                    