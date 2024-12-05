from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        print("check numCourses :", numCourses)

        prerequMap = {}

        for i in range(numCourses):
            prerequMap[i] = []

        for crs, pre in prerequisites:
            prerequMap[crs].append(pre)

        print("check prerequMap", prerequMap)
        
        

        visit = set()


        def dfs(crs):

            if crs in visit:
                return False
            
            if  



        # # looping through the course number 

        for i in range(numCourses):

            if not dfs(i):
                

            
            # print("check i", i)

if __name__ == "__main__":
    sol = Solution()
    
    # generate cycle test case w/o cycle
    # print(sol.canFinish(4, [[1, 0], [2, 1], [3, 2]]))
    
    # Cycle test case with cycle
    # print("checking final result", sol.canFinish(4, [[1, 0], [2, 1], [3, 2], [1, 3]]))
    
    # generate another test case with cycle w/ 5 numCourses
    print(sol.canFinish(5, [[1, 0], [2, 1], [3, 2], [4, 3], [3, 4]]))
    


        