from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows, columns = len(grid), len(grid[0])

        queue = deque()
        visited = set()
        island = 0

        # def bfs(r, c):

        direction = [[1,0],[-1,0], [0,1], [0,-1]]

        for dr, dc in direction:
            print("check dr", dr, "dc", dc)
            # for dc in direction:
            #     print("check dr [1,0]", dr, "dc", dc)
                # for column in direction: 

            # while queue:

        # print("Check ", type(1,0,3))

        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 1 and (r,c) not in visited:
                    bfs(r,c)
                    island+=1 

                # print("Check grid r :",r,"c :",c,"grid[r,c]:", grid[r][c])
                # print("check r", r, "c", c)

        # for r in row:
        #     print("check r" r)
            # for c in column:
                


        #         if column == 1 and column not in visited:
        #             bfs(column)
        #             island+= 1



        # return island
                    

                        

        