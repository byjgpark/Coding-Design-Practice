from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # print("Check prerequisites ", prerequisites)

        preMap = {}
        for i in range(numCourses):
            preMap[i] =[]

        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        #   print("Check crs", crs, "pre", pre)  
        print("check preMap", preMap)
        
        visit = set()
        
        def dfs(crs):
            
            if crs in visit:
                return False
            
            if preMap[crs] == []:
                return True
            
            visit.add(crs)
            
            for pre in preMap[crs]:
                if not dfs(pre):
                    visit.remove(pre)
                    return False
 
            visit.remove(crs)
            preMap[crs] = []
            return True   
        
        for i in range(numCourses):
            
            if not dfs(i):
                return False
            
        return True
        
if __name__ == "__main__":
    sol = Solution()
    
    # generate cycle test case w/o cycle
    # print(sol.canFinish(4, [[1, 0], [2, 1], [3, 2]]))
    
    # Cycle test case with cycle
    # print("checking final result", sol.canFinish(4, [[1, 0], [2, 1], [3, 2], [1, 3]]))
    
    # generate another test case with cycle w/ 5 numCourses
    print(sol.canFinish(5, [[1, 0], [2, 1], [3, 2], [4, 3], [3, 4]]))
    


        