from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        rows, columns = len(grid), len(grid[0])

        # print("check rows", rows, "columns", columns)

        visited = set()
        island = 0
        

        def bfs(r,c):
            # print("hello world")
            queue = deque()    
            visited.add((r,c))
            queue.append((r,c))
            # print("Check visited", visited, "queue", queue)
            while queue:
                print("check queue", queue)
                row, column = queue.popleft()
                direction = [[1,0], [-1,0], [0,1], [0, -1]]

                for dr, dc in direction:
                    nr, nc = row + dr, column + dc

                    if nr in range(rows) and nc in range(columns) and grid[nr][nc] == 1 and (nr, nc) not in visited:
                        visited.add((nr,nc))
                        queue.append((nr,nc))
                        
                    

        for row in range(rows):
            for column in range(columns):
                
                if grid[row][column] == 1 and (row,column) not in visited:
                    bfs(row, column)
                    island+=1
        
        return island

        #time complexity: O(row x column)        
        #space complexity: O(row x column)