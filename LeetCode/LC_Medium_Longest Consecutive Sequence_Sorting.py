class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res = 0
        nums.sort()

        curr, streak = nums[0], 0
        i = 0
        while i < len(nums):
            if curr != nums[i]:
                curr = nums[i]
                streak = 0
            while i < len(nums) and nums[i] == curr:
                i += 1
            streak += 1
            curr += 1
            res = max(res, streak)
        return res

#2 trial

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums.sort()
        i = 0
        streak, curr = 0, nums[0]

        print("check streak =", streak, " curr =", curr)

        while i < len(nums):

            if curr != nums[i]:
                curr = 0
                streak = 0

            while curr == nums[i]:
                i+=1

            curr+=1
            streak+=1
             
# 3rd trial

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        curr, streak = nums[0], 0
        nums.sort()
        i = 0
        res = 0

        # print("check nums[5]", nums[5])

        while i < len(nums):

            print("check i =",i)
            
            if nums[i]!= curr:
                curr = nums[i]
                streak = 0

            while i < len(nums) and nums[i] == curr:
                i+=1
            
            curr+=1
            streak+=1
            res = max(res, streak)
        return res
