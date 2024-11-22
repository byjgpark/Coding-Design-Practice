from collections import deque
from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def capture():
            q = deque()
            print("Initial board:")
            for row in board:
                print(row)
            
            # Step 1: Add border 'O' cells to the queue
            for r in range(ROWS):
                for c in range(COLS):
                    print("check r :",r,"c :",c)
                    if (r == 0 or r == ROWS - 1 or 
                        c == 0 or c == COLS - 1) and board[r][c] == "O":
                        q.append((r, c))
                        print(f"Added to queue: ({r}, {c})")
            
            # Step 2: Process the queue
            while q:
                r, c = q.popleft()
                print(f"Popped from queue: ({r}, {c})")
                if board[r][c] == "O":
                    board[r][c] = "T"
                    print(f"Marked ({r}, {c}) as 'T'")
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < ROWS and 0 <= nc < COLS:
                            q.append((nr, nc))
                            print(f"Neighbor added to queue: ({nr}, {nc})")
            
            print("Board after marking border-connected regions:")
            for row in board:
                print(row)
        
        capture()
        
        # Step 3: Transform the board
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    print(f"Changing ({r}, {c}) from 'O' to 'X'")
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    print(f"Changing ({r}, {c}) from 'T' to 'O'")
                    board[r][c] = "O"
        
        print("Final board:")
        for row in board:
            print(row)

if __name__ == "__main__":
    solution = Solution()
    
    board = [
        ["O", "X", "X", "X", "X"],
        ["X", "O", "O", "O", "X"],
        ["X", "X", "O", "O", "X"],  
        ["X", "O", "X", "X", "O"],
        ["X", "O", "O", "O", "X"]
    ]
    
    
    solution.solve(board)
    