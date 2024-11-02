import collections
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        print("\n=== Initial Grid ===")
        self.print_grid(grid)
        
        q = collections.deque()
        fresh = 0
        time = 0
        
        # Count fresh oranges and find initial rotten ones
        print("\n=== Finding initial state ===")
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                    print(f"Found fresh orange at ({r}, {c})")
                if grid[r][c] == 2:
                    q.append((r, c))
                    print(f"Found rotten orange at ({r}, {c})")
        
        print(f"\nInitial state: {fresh} fresh oranges, {len(q)} rotten oranges")
        
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        while fresh > 0 and q:
            
            # print("check q:", len(q))
            
            length = len(q)
            print(f"\n=== Minute {time} ===")
            print(f"Processing {length} rotten oranges in queue")
            
            for i in range(length):
                r, c = q.popleft()
                print(f"\nProcessing rotten orange at ({r}, {c})")
                
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    print(f"Checking adjacent cell ({row}, {col})", end=" ")
                    
                    # Check if in bounds
                    if row not in range(len(grid)) or col not in range(len(grid[0])):
                        print("- Out of bounds")
                        continue
                        
                    # Check if fresh orange
                    if grid[row][col] != 1:
                        print("- Not a fresh orange")
                        continue
                    
                    print("- Fresh orange found! Rotting it...")
                    grid[row][col] = 2
                    q.append((row, col))
                    fresh -= 1
                    print(f"Remaining fresh oranges: {fresh}")
            
            print("\nGrid after minute", time)
            self.print_grid(grid)
            time += 1
        
        final_result = time if fresh == 0 else -1
        print(f"\n=== Final Result ===")
        print(f"Time taken: {final_result}")
        print(f"Remaining fresh oranges: {fresh}")
        return final_result
    
    def print_grid(self, grid):
        print("   " + " ".join(f"{i}" for i in range(len(grid[0]))))
        for i, row in enumerate(grid):
            print(f"{i}: {row}")
            
if __name__ == "__main__":
    
    sol = Solution()
    print(sol.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))

# https://claude.site/artifacts/cdc66d46-7ca7-4032-b7bc-0cf7e5b4b05a

#my 1st attempt 
# from collections import deque 

# class Solution:
#     def orangesRotting(self, grid: List[List[int]]) -> int:

#         rows, columns = len(grid), len(grid[0])

#         # print("check ", type(grid[0][0]))

#         # print("check rows", rows, "check columns", columns)

#         q = deque([])  
        
#         fresh = 0
        
#         for row in range(rows):
#             for column in range(columns):

#                 if grid[row][column] == 1:
#                     fresh += 1

#                 elif grid[row][column] == 2:
#                     q.append((row, column))

#                 direction = [[0,1], [0,-1], [1,0], [-1,0]]

#                 while fresh > 0 and q:
#                     r, c = q.popleft()

#                     print("r :",r, "c", c)

#                     for dr, dc in direction:
#                         new_dr, new_dc = r+dr, c+dc


                        



#                     # for r




#                     print("check r",r, "c", c)


                    


        



                