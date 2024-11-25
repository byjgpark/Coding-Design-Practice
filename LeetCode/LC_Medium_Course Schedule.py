from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Map each course to its prerequisites
        print("\n=== Starting Course Schedule Check ===")
        print(f"Total courses: {numCourses}")
        print(f"Prerequisites: {prerequisites}")
        
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
            
        print(f"\nInitial prerequisite map: {preMap}")
        
        # Store all courses along the current DFS path
        visiting = set()
        
        def dfs(crs, depth=""):
            indent = "  " * len(depth)  # Create indentation based on recursion depth
            
            print(f"\n{indent}→ Entering DFS for course {crs}")
            print(f"{indent}  Current path: {list(visiting)} → {crs}")
            
            if crs in visiting:
                print(f"{indent}  ⚠️ Cycle detected! Course {crs} is already in path")
                print(f"{indent}  ↩️ Backtracking from course {crs} (cycle found)")
                return False
                
            if preMap[crs] == []:
                print(f"{indent}  ✓ Course {crs} has no prerequisites")
                print(f"{indent}  ↩️ Backtracking from course {crs} (no prerequisites)")
                return True
                
            visiting.add(crs)
            print(f"{indent}  Added course {crs} to current path: {list(visiting)}")
            
            for pre in preMap[crs]:
                print(f"{indent}  Checking prerequisite {pre} for course {crs}")
                if not dfs(pre, depth + "  "):
                    print(f"{indent}  ❌ Failed at prerequisite {pre} for course {crs}")
                    print(f"{indent}  ↩️ Backtracking from course {crs} (prerequisite failed)")
                    return False
                print(f"{indent}  ✓ Prerequisite {pre} is valid for course {crs}")
                    
            visiting.remove(crs)
            print(f"{indent}  Removed course {crs} from current path: {list(visiting)}")
            
            preMap[crs] = []
            print(f"{indent}  Marked course {crs} as completed (cleared prerequisites)")
            
            print(f"{indent}  ✓ Successfully verified course {crs}")
            print(f"{indent}  ↩️ Backtracking from course {crs} (success)")
            return True
            
        for c in range(numCourses):
            print(f"\n=== Starting verification for course {c} ===")
            if not dfs(c):
                print(f"\n❌ Cannot complete course {c} - cycle detected in prerequisites")
                return False
            print(f"✓ Course {c} can be completed")
            
        print("\n✓ All courses can be completed successfully!")
        return True

if __name__ == "__main__":
    sol = Solution()
    
    # generate other test cases
    # print(sol.canFinish(2, [[1, 0]]))
    # print(sol.canFinish(2, [[1, 0], [0, 1]]))
    # print(sol.canFinish(3, [[1, 0], [2, 1]]))
    # print(sol.canFinish(3, [[1, 0], [2, 1], [0, 2]]))
    # print(sol.canFinish(4, [[1, 0], [2, 1], [3, 2], [1, 3]]))
    
    # generate no cycle test case
    print(sol.canFinish(4, [[1, 0], [2, 1], [3, 2]]))