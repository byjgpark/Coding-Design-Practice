from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        print(f"\nInitial board state:")
        self.print_board(board)
        
        def capture(r, c, depth=0):
            indent = "  " * depth  # Indentation for recursive depth visualization
            print(f"{indent}→ Entering capture() at position r={r}, c={c}")
            
            # Check boundary conditions and valid 'O'
            if (r < 0 or c < 0 or r == ROWS or c == COLS):
                print(f"{indent}  Out of bounds, returning")
                return
            if board[r][c] != "O":
                print(f"{indent}  Not an 'O' (found '{board[r][c]}'), returning")
                return
            
            # Mark current cell
            print(f"{indent}  Marking position ({r},{c}) from 'O' to 'T'")
            board[r][c] = "T"
            print(f"{indent}  Current board state:")
            self.print_board(board, indent + "    ")
            
            # Recursive calls in all four directions
            print(f"{indent}  Exploring neighbors:")
            directions = [(1,0,"down"), (-1,0,"up"), (0,1,"right"), (0,-1,"left")]
            for dr, dc, direction in directions:
                new_r, new_c = r + dr, c + dc
                print(f"{indent}    Checking {direction} neighbor at ({new_r},{new_c})")
                capture(new_r, new_c, depth + 1)
            
            print(f"{indent}← Returning from capture() at position r={r}, c={c}")
        
        # Process border cells
        print("\nChecking left and right borders:")
        for r in range(ROWS):
            if board[r][0] == "O":
                print(f"\nFound 'O' at left border ({r},0)")
                capture(r, 0)
            if board[r][COLS - 1] == "O":
                print(f"\nFound 'O' at right border ({r},{COLS-1})")
                capture(r, COLS - 1)
        
        print("\nChecking top and bottom borders:")
        for c in range(COLS):
            if board[0][c] == "O":
                print(f"\nFound 'O' at top border (0,{c})")
                capture(0, c)
            if board[ROWS - 1][c] == "O":
                print(f"\nFound 'O' at bottom border ({ROWS-1},{c})")
                capture(ROWS - 1, c)
        
        print("\nFinal conversion phase:")
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    print(f"Converting surrounded 'O' to 'X' at ({r},{c})")
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    print(f"Converting border-connected 'T' back to 'O' at ({r},{c})")
                    board[r][c] = "O"
        
        print("\nFinal board state:")
        self.print_board(board)
    
    def print_board(self, board, indent=""):
        """Helper function to print board state"""
        for row in board:
            print(indent + " ".join(row))

if __name__ == "__main__":
    # Example usage:
    board = [
    ["X", "X", "X", "X"],
    ["X", "O", "O", "X"],
    ["X", "X", "O", "X"],
        ["X", "O", "X", "X"]
    ]
    solution = Solution()
    print("Running surrounded regions solution with debug output:")
    solution.solve(board)