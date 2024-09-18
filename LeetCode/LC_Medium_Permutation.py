from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        # base case
        if len(nums) == 1:
            return [nums[:]]  # nums[:] is a deep copy

        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)
            
            print("Check perms: ", perms)

            for perm in perms:
                perm.append(n)
            res.extend(perms)
            nums.append(n)
        return res
    
if __name__ == "__main__":
    s = Solution()
    nums = [1, 2, 3]
    s.permute(nums)
    # print(s.perm)