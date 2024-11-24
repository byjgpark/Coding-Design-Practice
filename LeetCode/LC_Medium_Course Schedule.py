from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Map each course to its prerequisites
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
            
        print(f"\nInitial prerequisite map: {preMap}")
        
        # Store all courses along the current DFS path
        visiting = set()
        
        def dfs(crs, depth=""):
            indent = "  " * len(depth)  # Create indentation based on recursion depth
            
            print(f"\n{indent}Starting DFS for course {crs}")
            print(f"{indent}Current visiting set: {visiting}")
            print(f"{indent}Current prerequisite map: {preMap}")
            
            if crs in visiting:
                print(f"{indent}Cycle detected! Course {crs} is already being visited")
                return False
                
            if preMap[crs] == []:
                print(f"{indent}No prerequisites for course {crs}, returning True")
                return True
                
            visiting.add(crs)
            print(f"{indent}Added course {crs} to visiting set: {visiting}")
            
            for pre in preMap[crs]:
                print(f"{indent}Checking prerequisite {pre} for course {crs}")
                if not dfs(pre, depth + "  "):
                    print(f"{indent}Failed at prerequisite {pre} for course {crs}")
                    return False
                    
            visiting.remove(crs)
            print(f"{indent}Removed course {crs} from visiting set: {visiting}")
            
            preMap[crs] = []
            print(f"{indent}Cleared prerequisites for course {crs}: {preMap[crs]}")
            
            print(f"{indent}Successfully completed course {crs}")
            return True
            
        for c in range(numCourses):
            print(f"\nStarting new course check: {c}")
            if not dfs(c):
                print(f"Cannot complete course {c}, detecting cycle or invalid prerequisites")
                return False
            print(f"Successfully verified course {c} can be completed")
            
        print("\nAll courses can be completed!")
        return True

if __name__ == "__main__":
    sol = Solution()
    
    # generate other test cases
    # print(sol.canFinish(2, [[1, 0]]))
    # print(sol.canFinish(2, [[1, 0], [0, 1]]))
    # print(sol.canFinish(3, [[1, 0], [2, 1]]))
    # print(sol.canFinish(3, [[1, 0], [2, 1], [0, 2]]))
    print(sol.canFinish(4, [[1, 0], [2, 1], [3, 2], [1, 3]]))