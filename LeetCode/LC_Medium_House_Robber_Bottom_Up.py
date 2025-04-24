# from typing import List

# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         print("Input array:", nums)
        
#         if not nums:
#             print("Empty array, returning 0")
#             return 0
#         if len(nums) == 1:
#             print("Only one house with value", nums[0])
#             return nums[0]
        
        
#         dp = [0] * len(nums)
#         dp[0] = nums[0]
#         dp[1] = max(nums[0], nums[1])
        
        
#         print("\nInitializing dp array:", dp)
#         print(f"Initial dp[0] = {dp[0]} (value of first house)")
#         print(f"Initial dp[1] = {dp[1]} (max of first and second house)")
        
#         for i in range(2, len(nums)):
        
        
#             # Option 1: Skip current house, take previous max
#             option1 = dp[i - 1]
#             # Option 2: Rob current house, take max from two houses ago
#             option2 = nums[i] + dp[i - 2]
            
#             print(f"At house {i} (value: {nums[i]}):")
#             print(f"  Option 1: Skip this house, keep previous max = {option1}")
#             print(f"  Option 2: Rob this house + max from 2 houses ago = {nums[i]} + {dp[i-2]} = {option2}")
            
#             dp[i] = max(option1, option2)
#             print(f"  Choosing max: dp[{i}] = {dp[i]}")
        
#         print("\nFinal dp array:", dp)
#         print("Each index represents the maximum amount that can be robbed up to that house")
#         return dp[-1]

# if __name__ == "__main__":
    
#     solution = Solution()
#     nums = [2, 7, 9, 3, 1]
#     print("\nRunning house robber with input:", nums)
#     result = solution.rob(nums)
#     print("\nFinal Result:", result)


class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        dp = [-1] * len(nums)

        print("check dp ", dp)
        
        dp[0] = nums[0]

        dp[1] = max(nums[0], nums[1])

        print("check dp ", dp)

        for i in range(2, len(nums)):

            print("check nums[i]", nums[i])

            option1 = dp[i-1] 
            option2 = nums[i] + dp[i-2]

            dp[i] = max(option1, option2)

        # print("dp")

        print("check dp ", dp)

        return dp[-1]