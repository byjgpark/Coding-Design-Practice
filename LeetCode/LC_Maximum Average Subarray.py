class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        # 1, find max num til k
        # 2, sliding windiw -> subtracking left pointer and adding right pointer from the sum
        # 3, find the max => find average 

        maxNum = sum(nums[:k])

        print("check maxNum", maxNum)



       


       