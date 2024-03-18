class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        # 1, find max num til k
        # 2, sliding windiw -> subtracking left pointer and adding right pointer from the sum
        # 3, find the max => find average 
        L = 0
        R = k-1
        maxNum = sum(nums[:k])

        arr = []

        print("check L", L,"R", R)

        print("check maxNum", maxNum)

        # while L < R:
        #     if( R == 5):
        for element in nums:
            if( R == k+1):
                break
            maxNum -= nums[L]
            
            L +=1 
            R +=1
            maxNum += nums[R]
            print("check maxNum", maxNum)
            arr.append(maxNum)

        


           
            # break
            
            



        



       


       