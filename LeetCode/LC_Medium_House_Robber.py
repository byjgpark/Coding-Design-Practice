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
    nums = [2, 7, 9, 3, 1]
    print("\nFinal Result:", solution.rob(nums))
    
    
#     dfs(0) [Start at index 0]
# ├── Option 1: Skip House 0 (value 2)
# │     └── dfs(1)
# │          ├── Option 1: Skip House 1 (value 7)
# │          │     └── dfs(2)
# │          │          ├── Option 1: Skip House 2 (value 9)
# │          │          │     └── dfs(3)
# │          │          │          ├── Option 1: Skip House 3 (value 3)
# │          │          │          │     └── dfs(4)
# │          │          │          │          ├── Option 1: Skip House 4 (value 1)
# │          │          │          │          │     └── dfs(5) → returns 0
# │          │          │          │          └── Option 2: Rob House 4 (1 + dfs(6)=1+0)
# │          │          │          │                → returns 1
# │          │          │          │     => dfs(4) returns max(0, 1) = 1
# │          │          │          └── Option 2: Rob House 3 (3 + dfs(5)=3+0)
# │          │          │                → returns 3
# │          │          │     => dfs(3) returns max(1, 3) = 3
# │          │          └── Option 2: Rob House 2 (9 + dfs(4)=9+1)
# │          │                → returns 10
# │          │     => dfs(2) returns max(3, 10) = 10
# │          └── Option 2: Rob House 1 (7 + dfs(3)=7+3)
# │                → returns 10
# │     => dfs(1) returns max(10, 10) = 10
# └── Option 2: Rob House 0 (2 + dfs(2)=2+10)
#       → returns 12
# => dfs(0) returns max(10, 12) = 12
