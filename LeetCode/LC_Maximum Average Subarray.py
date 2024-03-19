class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        L = 0
        R = k

        sumNum = 0

        for i in range(k):
            sumNum +=nums[i]

        newSum = sumNum

        while R < len(nums):
            newSum -= nums[L]
            L+=1
            newSum += nums[R]
            R+=1

            sumNum = max(newSum, sumNum)
        
        return sumNum/ k
            

        

            


    




            
            



        



       


       