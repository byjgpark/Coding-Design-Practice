
from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []
        
        print("chek")
        
        print("hi I need to check")

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            # decision to include nums[i]
            subset.append(nums[i])
            
            ## dfs(1), dfs(2)
            dfs(i + 1) 
            
            print("returned to here 1")
            # decision NOT to include nums[i]
            subset.pop()
            ## dfs(3)
            dfs(i + 1) 
            print("returned to here 1")


        dfs(0)
        return res
    
    # its so hard bro, so I will master it !! since it's really hard
