class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # for i in nums:
        #     print("check i", i)

        for i in range(len(nums)):
            print("check i", i)
        
        for i in nums:
            for j in nums:
                if i + j == target:
                    return [i, j]