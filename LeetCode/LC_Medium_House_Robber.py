from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        def dfs(i, depth=0):
            indent = "  " * depth  # Visualize recursion depth
            print(f"{indent}→ dfs({i}) [Depth {depth}]")

            # Base case
            if i >= len(nums):
                print(f"{indent}  ↳ Base case (i={i} >= {len(nums)}), return 0")
                return 0

            # Recursive cases
            print(f"{indent}  Computing max(skip house {i} → dfs({i+1}), rob house {i} → {nums[i]} + dfs({i+2}))")
            
            skip = dfs(i + 1, depth + 1)
            print(f"{indent}  ↳ Result from skipping house {i}: {skip}")
            
            rob = nums[i] + dfs(i + 2, depth + 1)
            print(f"{indent}  ↳ Result from robbing house {i}: {rob} (including nums[{i}] = {nums[i]})")
            
            result = max(skip, rob)
            print(f"{indent}  Returning max({skip}, {rob}) = {result} from dfs({i})")
            return result
        
        final_result = dfs(0)
        print("\nFinal maximum amount you can rob:", final_result)
        return final_result

# Example usage:
# sol = Solution()
# print(sol.rob([1, 2, 3]))  # Test with sample input

if __name__ == "__main__":
    sol = Solution()
    sol.rob([2,7,9,3,1])