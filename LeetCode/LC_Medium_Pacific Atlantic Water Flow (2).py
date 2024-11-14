class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        row, col = len(heights), len(heights[0])

        print("check here row :", row, "col :", col)

        atl, pac = set(), set()

        def dfs(r,c, visited, previValue):

            if (r < 0 or c < 0) or ( r not in range(row) or c not in range(col)) or ((r,c) in visited) or ( heights[r][c] < previValue):
                return  

            visited.add((r,c))

            # print("Check (r,c)", (r,c))
            # print("check previValue :", previValue)
            dfs(r+1, c, visited, heights[r][c])
            dfs(r-1, c, visited, heights[r][c])
            dfs(r, c+1, visited, heights[r][c])
            dfs(r, c-1, visited, heights[r][c])

        # column
        for c in range(col):
            dfs(0, c, pac, heights[0][c])
            dfs(row-1, c, atl, heights[row-1][c])

        # row
        for r in range(row):

            print("check r in the loop", r)
            dfs(r, 0, pac, heights[r][0])
            dfs(r, col-1, atl, heights[r][col-1])

        # find duplicate value from set 
        print("check pac" , len(pac))
        print("check alt", len(atl))
        
        result = []
        
        for p in pac:
            for a in atl:
                if p == a:
                    result.append(p)
        
        print("check result", result)
        return result

