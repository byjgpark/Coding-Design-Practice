from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows, columns = len(grid), len(grid[0])

        print("Check rows", rows, "columns", columns)

        queue = deque()
        visited = set()
        island = 0

        def bfs(r, c):

            direction = [[1,0],[-1,0],[0,1],[0,-1]]

            print("Check r", r, "c", c)

            queue.append()

            for dr, dc in direction:
                new_dr, new_dc = dr + r, dc + c

                while queue:
                # print("check rows", range(rows-1), "column", range(columns-1))
                    if new_dr in range(rows-1) and new_dc in range(columns-1) and grid[new_dr][new_dc] == "1" and (new_dr, new_dc) not visted:
                        


                    print("check new_dr", new_dr, "new_dc", new_dc)

            
            # print("check dr", dr, "dc", dc)
            # for dc in direction:
            #     print("check dr [1,0]", dr, "dc", dc)
                # for column in direction: 

            # while queue:

        # print("Check ", type(1,0,3))

        for r in range(rows):
            for c in range(columns):
                # print("check here r", r,"c",c)
                if grid[r][c] == "1" and (r,c) not in visited:
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
                    

                        

        