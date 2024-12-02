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

        # def dfs(crs):

            # if crs in visit: 



        # looping through the course number 

        # for i in range(numCourses):

            

            
            # print("check i", i)





        