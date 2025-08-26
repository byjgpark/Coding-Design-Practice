# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         numSet = set(nums)
#         longest = 0

#         for num in numSet:
#             if (num - 1) not in numSet:
#                 length = 1
#                 while (num + length) in numSet:
#                     length += 1
#                 longest = max(length, longest)
#         return longest

# # 1st trial
# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         numSet = set(nums)
#         longest = 0

#         for num in numSet:
#             if (num - 1) not in numSet:
#                 length = 1
#                 while (num + length) in numSet:
#                     length += 1
#                 longest = max(length, longest)
#         return longest

# 2nd trial
from collections import defaultdict
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mp = defaultdict(int)
        res = 0

        for num in nums:
            if not mp[num]:
                print(f"\nProcessing num = {num}")
                left = mp[num - 1]
                right = mp[num + 1]
                print(f"Left neighbor {num-1} has length: {left}")
                print(f"Right neighbor {num+1} has length: {right}")
                
                current_length = left + right + 1
                mp[num] = current_length
                print(f"New length for {num}: {current_length}")
                
                # Update boundaries
                if left > 0:
                    left_boundary = num - left
                    mp[left_boundary] = current_length
                    print(f"Updated left boundary {left_boundary} to {current_length}")
                if right > 0:
                    right_boundary = num + right
                    mp[right_boundary] = current_length
                    print(f"Updated right boundary {right_boundary} to {current_length}")
                
                res = max(res, current_length)
                print(f"Current max length: {res}")
                print(f"Current state of map: {dict(mp)}")
                
                
                
        return res

# At line 68, add the missing closing parenthesis
if __name__ == "__main__":
    nums = [100, 4, 200, 1, 3, 2]
    sol = Solution()
    print(sol.longestConsecutive(nums))