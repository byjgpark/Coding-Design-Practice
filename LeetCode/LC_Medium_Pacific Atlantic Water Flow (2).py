class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        row, col = len(heights), len(heights[0])

        print("check here row :", row, "col :", col)

        atl, pac = set(), set()

        def dfs(r,c, visited, previValue):

            if (r < 0 or c < 0) or ( r not in range(row) or c not in range(col)) or ((r,c) in visited) or ( heights[r][c] < previValue):
                return  

            visited.add((r,c))

            print("Check (r,c)", (r,c))
            # print("check previValue :", previValue)
            dfs(r+1, c, visited, previValue)
            dfs(r-1, c, visited, previValue)
            dfs(r, c+1, visited, previValue)
            dfs(r, c-1, visited, previValue)

        # column
        for c in range(col):
            dfs(0, c, pac, heights[0][c])
            # dfs(col-1, c, atl, heights[col-1][c])

        # row
        print("check pac", pac)
        