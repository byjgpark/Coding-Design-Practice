from collections import deque
from typing import List

# BFS Version From Video
class SolutionBFS:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        
        # print("check rows, cols", rows, cols)
        
        visited = set()
        islands = 0

        def bfs(r, c):
             q = deque()
             visited.add((r, c))
             q.append((r, c))
             
             print("check visited", visited)
             print("q", q)
           
             while q:
                 row, col = q.popleft()
                #  print("check row, col", row, col)
                 directions = [[1, 0],[-1, 0],[0, 1],[0, -1]]
               
                 for dr, dc in directions:
                     r, c = row + dr, col + dc
                     if (r) in range(rows) and (c) in range(cols) and grid[r][c] == '1' and (r, c) not in visited:
                       
                         q.append((r, c ))
                         visited.add((r, c ))

        for r in range(rows):
            for c in range(cols):
                
                if grid[r][c] == "1" and (r, c) not in visited:
                    print("check r, c", r, c)
                    bfs(r, c)
                    islands += 1 

        return islands
    
if __name__ == "__main__":
    grid = [
            ["1","1","0","0"],
            ["1","1","0","0"],
            ["0","0","1","0"],
            ["0","0","0","1"]
            ]
    
    solution = SolutionBFS()
    print(solution.numIslands(grid))