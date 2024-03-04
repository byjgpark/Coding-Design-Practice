
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashmap = {}

        for i in range(len(nums)):
        
            complement = target - nums[i]
            
            # print("check hashmap", hashmap)

            # print("check complment", complement)    

            if complement in hashmap:
                return [hashmap[complement], i]
            hashmap[nums[i]] = i 