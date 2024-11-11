from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        
        print(f"\nGrid Dimensions: {ROWS}x{COLS}")
        print("Initial Heights Grid:")
        for row in heights:
            print(row)
            
        pac, atl = set(), set()
        
        def dfs(r, c, visit, prevHeight, depth="", parent=None):
            indent = "  " * len(depth)
            print(f"\n{indent}→ DFS Enter: ({r}, {c}) [Depth: {depth}]")
            if parent:
                print(f"{indent}Called from: ({parent[0]}, {parent[1]})")
            print(f"{indent}Previous Height: {prevHeight}")
            
            # Check and print all conditions
            conditions = {
                "In visit set": (r, c) in visit,
                "Row < 0": r < 0,
                "Col < 0": c < 0,
                "Row >= ROWS": r >= ROWS,
                "Col >= COLS": c >= COLS,
            }
            
            if r >= 0 and r < ROWS and c >= 0 and c < COLS:
                conditions["Height too low"] = heights[r][c] < prevHeight
            
            print(f"{indent}Checking conditions:")
            for condition, result in conditions.items():
                print(f"{indent}  {condition}: {result}")
                
            if any(conditions.values()):
                if parent:
                    print(f"{indent}← Backtracking: Failed condition check at ({r}, {c}), returning to ({parent[0]}, {parent[1]})")
                else:
                    print(f"{indent}← Backtracking: Failed condition check at ({r}, {c}), returning to initial call")
                return
                
            current_height = heights[r][c]
            print(f"{indent}Current cell height: {current_height}")
            
            visit.add((r, c))
            print(f"{indent}Added ({r}, {c}) to visit set")
            print(f"{indent}Current visit set: {visit}")
            
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc
                direction_name = {
                    (1, 0): "↓ DOWN",
                    (-1, 0): "↑ UP",
                    (0, 1): "→ RIGHT",
                    (0, -1): "← LEFT"
                }[dr, dc]
                print(f"\n{indent}Exploring {direction_name}: ({new_r}, {new_c})")
                dfs(new_r, new_c, visit, current_height, depth + "→", (r, c))
            
            if parent:
                print(f"{indent}← Backtracking: Completed all directions at ({r}, {c}), returning to ({parent[0]}, {parent[1]})")
            else:
                print(f"{indent}← Backtracking: Completed all directions at ({r}, {c}), returning to initial call")
        
        print("\nStarting Pacific DFS from top edge:")
        for c in range(COLS):
            print(f"\nStarting from (0, {c})")
            dfs(0, c, pac, heights[0][c], "P")
            
        print("\nStarting Pacific DFS from left edge:")
        for r in range(ROWS):
            print(f"\nStarting from ({r}, 0)")
            dfs(r, 0, pac, heights[r][0], "P")
            
        print("\nFinal Pacific set:", pac)
        
        print("\nStarting Atlantic DFS from bottom edge:")
        for c in range(COLS):
            print(f"\nStarting from ({ROWS-1}, {c})")
            dfs(ROWS - 1, c, atl, heights[ROWS-1][c], "A")
            
        print("\nStarting Atlantic DFS from right edge:")
        for r in range(ROWS):
            print(f"\nStarting from ({r}, {COLS-1})")
            dfs(r, COLS - 1, atl, heights[r][COLS-1], "A")
            
        print("\nFinal Atlantic set:", atl)
        
        res = []
        print("\nFinding intersection points:")
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    print(f"Found intersection at ({r}, {c})")
                    res.append([r, c])
        
        print("\nFinal Result:", res)
        return res

if __name__ == "__main__":
    sol = Solution()
    print(sol.pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))