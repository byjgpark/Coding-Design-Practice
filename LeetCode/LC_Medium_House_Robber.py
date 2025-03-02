from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        def dfs(i, depth=0):
            indent = "  " * depth
            print(f"\n{indent}Entering dfs for index i = {i}")
            if i >= len(nums):
                print(f"{indent}Base case: i={i} is beyond the array. Returning 0.")
                return 0
            
            # Option 1: Skip current house and go to i + 1
            print(f"{indent}Option 1: Skipping house {i} (value {nums[i] if i < len(nums) else 'N/A'}) and jumping to i+1")
            option1 = dfs(i + 1, depth + 1)
            print(f"{indent}Returned from DFS call for i={i+1} with value: {option1}")
            
            # Option 2: Rob current house and go to i + 2
            print(f"{indent}Option 2: Robbing house {i} (value {nums[i]}) and jumping to i+2")
            option2 = nums[i] + dfs(i + 2, depth + 1)
            print(f"{indent}Returned from DFS call for i={i+2} with accumulated value: {option2}")
            
            # Calculate the maximum of both options
            best_option = max(option1, option2)
            print(f"{indent}At index {i}, the best option is max({option1}, {option2}) = {best_option}")
            
            
            return best_option
        
        return dfs(0)

# Example usage
if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 3, 1]
    print("\nFinal Result:", solution.rob(nums))