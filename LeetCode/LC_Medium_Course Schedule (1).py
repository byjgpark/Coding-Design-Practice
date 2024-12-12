from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        print("\n=== Starting Course Schedule Check ===")
        print(f"Total courses: {numCourses}")
        print(f"Prerequisites: {prerequisites}")
        
        # Map each course to its prerequisites
        preMap = {i: [] for i in range(numCourses)}
        
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
            
        print(f"\nInitial prerequisite map: {preMap}")
        
        # Store all courses along the current DFS path
        visiting = set()
        
        
        def dfs(crs, depth=0):
            indent = "  " * depth  # Create indentation based on recursion depth
            
            # ADDED: More detailed entry logging
            print(f"\n{indent}🟢 ENTRY POINT: Entering DFS for course {crs}")
            print(f"{indent}  Current recursion depth: {depth}")
            print(f"{indent}  Current visiting set before check: {list(visiting)}")
            print(f"{indent}  Current prerequisites for course {crs}: {preMap[crs]}")
            
            # Cycle detection
            if crs in visiting:
                print(f"\n{indent}🔴 CYCLE DETECTION POINT:")
                print(f"{indent}  ⚠️ Course {crs} is ALREADY in visiting set!")
                print(f"{indent}  Current visiting set: {list(visiting)}")
                print(f"{indent}  🚫 CYCLE DETECTED - Returning False")
                return False
            
            # No prerequisites case
            if preMap[crs] == []:
                print(f"\n{indent}🟢 NO PREREQUISITES CASE:")
                print(f"{indent}  Course {crs} has NO prerequisites")
                print(f"{indent}  ✅ Returning True")
                return True
            
            # Add current course to visiting set
            visiting.add(crs)
            print(f"\n{indent}📌 VISITING SET UPDATE:")
            print(f"{indent}  Added course {crs} to visiting set")
            print(f"{indent}  Updated visiting set: {list(visiting)}")
            
            # Check each prerequisite
            for pre in preMap[crs]:
                print(f"\n{indent}🔍 PREREQUISITE CHECK:")
                print(f"{indent}  Checking prerequisite {pre} for course {crs}")
                
                # Recursive DFS call
                dfs_result = dfs(pre, depth + 1)
                
                # Check result of DFS
                if not dfs_result:
                    print(f"\n{indent}❌ PREREQUISITE FAILURE:")
                    print(f"{indent}  Prerequisite {pre} FAILED for course {crs}")
                    print(f"{indent}  🚫 Returning False from prerequisite check")
                    
                    # ADDED: Detailed backtracking information
                    print(f"\n{indent}🔙 BACKTRACKING DETAILS:")
                    print(f"{indent}  Current visiting set before removal: {list(visiting)}")
                    visiting.remove(crs)
                    print(f"{indent}  Removed course {crs} from visiting set")
                    print(f"{indent}  Updated visiting set after removal: {list(visiting)}")
                    return False
                
                print(f"{indent}  ✅ Prerequisite {pre} for course {crs} is VALID")
            
            # Remove current course from visiting set after checking all prerequisites
            visiting.remove(crs)
            print(f"\n{indent}🔙 POST-PREREQUISITE CHECK:")
            print(f"{indent}  Removed course {crs} from visiting set")
            print(f"{indent}  Updated visiting set: {list(visiting)}")
            
            # Clear prerequisites to mark as completed
            preMap[crs] = []
            print(f"{indent}  Marked course {crs} as completed (cleared prerequisites)")
            
            # NEW: Print prerequisite status after clearing
            print(f"{indent}  📋 Prerequisites status AFTER clearing:")
            print(f"{indent}  Updated prerequisite map: {preMap}")
            
            print(f"\n{indent}✅ SUCCESSFUL VERIFICATION:")
            print(f"{indent}  Successfully verified course {crs}")
            return True
        
        # Check each course
        for c in range(numCourses):
            print(f"\n=== Starting verification for COURSE {c} ===")
            
            # Reset visited set for each course start
            visiting.clear()
            
            # Run DFS for current course
            if not dfs(c):
                print(f"\n❌ FINAL RESULT: Cannot complete course {c}")
                print("❌ Cycle detected in prerequisites")
                return False
            
            print(f"✅ Course {c} can be completed")
        
        print("\n🏁 FINAL RESULT:")
        print("✅ All courses can be completed successfully!")
        return True

if __name__ == "__main__":
    sol = Solution()
    
    # generate cycle test case w/o cycle
    # print(sol.canFinish(4, [[1, 0], [2, 1], [3, 2]]))
    
    # Cycle test case with cycle
    # print("checking final result", sol.canFinish(4, [[1, 0], [2, 1], [3, 2], [1, 3]]))
    
    # generate another test case with cycle w/ 5 numCourses
    print(sol.canFinish(5, [[1, 0], [2, 1], [3, 2], [4, 3], [3, 4]]))