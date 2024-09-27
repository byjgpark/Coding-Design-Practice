from typing import List

# class Solution:
#     def permute(self, nums: List[int], depth=0) -> List[List[int]]:
#         indent = "  " * depth  # Indentation based on recursion depth
#         print(f"{indent}Call depth {depth}: permute(nums={nums})")
#         res = []

#         # base case
#         if len(nums) == 1:
#             print(f"{indent}Base case reached with nums={nums}, returning {[nums[:]]}")
#             return [nums[:]]  # nums[:] is a deep copy

#         for i in range(len(nums)):
#             n = nums.pop(0)
#             print(f"{indent}Popped n={n}, nums now={nums}")
#             perms = self.permute(nums, depth + 1)
#             print(f"{indent}Received perms={perms} from permute(nums={nums})")

#             print(f"{indent}Appending n={n} to each perm in perms")
#             for perm in perms:
#                 perm.append(n)
#             print(f"{indent}checking res={res}")
#             res.extend(perms)
#             nums.append(n)
#             print(f"{indent}Appended n={n} back to nums, nums now={nums}")
#         print(f"{indent}Returning res={res}")
#         return res

# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         res = []

#         # base case
#         if len(nums) == 1:
#             return [nums[:]]  # nums[:] is a deep copy

#         for i in range(len(nums)):
#             n = nums.pop(0)
#             perms = self.permute(nums)

#             for perm in perms:
#                 perm.append(n)
#             res.extend(perms)
#             nums.append(n)
#         return res

    
# if __name__ == "__main__":
#     s = Solution()
#     nums = [1, 2, 3]
#     s.permute(nums)
#     # print(s.perm)


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []

        def backtrack(sol):
            if len(sol) == n:
                ans.append(sol[:])
                return

            for x in nums:
                print(f"x: {x}")
                if x not in sol:
                    sol.append(x)
                    backtrack(sol) # backtrack([1]), backtrack([1,2]), backtrack([1,2,3])
                    sol.pop()

        backtrack([])
        return ans
    
    

if __name__ == "__main__":
    s = Solution()
    nums = [1, 2, 3]
    print(s.permute(nums))
    
    # print(s.perm)

# analayze its time & space complexity
# Time Complexity: O(n!)
# Space Complexity: O(n)



    