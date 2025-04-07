# from typing import List

# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         def dfs(i, depth=0):
#             indent = "  " * depth
#             print(f"\n{indent}{'='*20}")
#             print(f"{indent}ENTERING DFS at index {i} (depth {depth})")
#             print(f"{indent}Current house value: {nums[i] if i < len(nums) else 'Out of bounds'}")
            
#             if i >= len(nums):
#                 print(f"{indent}Base case reached: Index {i} is beyond array.")
#                 print(f"{indent}RETURNING 0")
#                 return 0
            
#             # Option 1: Skip current house
#             print(f"\n{indent}Option 1: SKIP house {i} (value {nums[i]})")
#             print(f"{indent}├─ Moving to index {i+1}")
#             option1 = dfs(i + 1, depth + 1)
#             print(f"\n{indent}BACK FROM OPTION 1 (index {i+1})")
#             print(f"{indent}├─ Value returned: {option1}")
            
#             # Option 2: Rob current house
        
#             print(f"\n{indent}Option 2: ROB house {i} (value {nums[i]})")
#             print(f"{indent}├─ Adding value: {nums[i]}")
#             print(f"{indent}├─ Moving to index {i+2}")
#             option2 = nums[i] + dfs(i + 2, depth + 1)
            
#             print(f"\n{indent}BACK FROM OPTION 2 (index {i+2})")
#             print(f"{indent}├─ Accumulated value: {option2}")
            
            
#             # Determine best option
#             best = max(option1, option2)
            
#             print(f"\n{indent}DECISION at index {i}:")
#             print(f"{indent}├─ Option 1 (skip): {option1}")
#             print(f"{indent}├─ Option 2 (rob): {option2}")
#             print(f"{indent}└─ CHOSEN MAX: {best}")
#             print(f"{indent}RETURNING {best}")
#             print(f"{indent}{'='*20}")
            
#             return best
        
#         print("Starting recursion from index 0\n")
#         return dfs(0)

# # Example usage
# if __name__ == "__main__":
#     solution = Solution()
#     nums = [2, 7, 9, 3, 1]
#     print("\nFinal Result:", solution.rob(nums))




from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        def dfs(i, depth=0):
            indent = "  " * depth
            print(f"\n{indent}{'='*20}")
            print(f"{indent}ENTERING DFS at index {i} (depth {depth})")
            print(f"{indent}Current house value: {nums[i] if i < len(nums) else 'Out of bounds'}")
            
            if i >= len(nums):
                print(f"{indent}Base case reached: Index {i} is beyond array.")
                print(f"{indent}RETURNING 0")
                return 0
            
            # Option 1: Skip current house
            print(f"\n{indent}Option 1: SKIP house {i} (value {nums[i]})")
            print(f"{indent}├─ Moving to index {i+1}")
            option1 = dfs(i + 1, depth + 1)
            print(f"\n{indent}BACK FROM OPTION 1 (index {i+1})")
            print(f"{indent}├─ Value returned: {option1}")
            
            # Option 2: Rob current house
            print(f"\n{indent}Option 2: ROB house {i} (value {nums[i]})")
            print(f"{indent}├─ Adding current value: {nums[i]}")
            print(f"{indent}├─ Moving to index {i+2} (skipping next house)")
            print(f"{indent}│")
            print(f"{indent}└─ RECURSIVE CALL FOR INDEX {i+2}")
            rob_next = dfs(i + 2, depth + 1)
            print(f"\n{indent}RETURN FROM ROB_NEXT (index {i+2})")
            print(f"{indent}├─ Value from future houses: {rob_next}")
            option2 = nums[i] + rob_next
            
            
            
            
            print(f"{indent}├─ Total if we rob this house: {nums[i]} + {rob_next} = {option2}")
            
            
            # Determine best option
            best = max(option1, option2)
            
            print(f"\n{indent}DECISION at index {i}:")
            print(f"{indent}├─ Option 1 (skip): {option1}")
            print(f"{indent}├─ Option 2 (rob): {option2}")
            print(f"{indent}└─ CHOSEN MAX: {best}")
            print(f"{indent}RETURNING {best}")
            print(f"{indent}{'='*20}")
            
        
            return best
        
        
        print("Starting recursion from index 0\n")
        
        return dfs(0)

# Example usage
if __name__ == "__main__":
    solution = Solution()
    nums = [2, 7, 9, 3, 1]
    print("\nFinal Result:", solution.rob(nums))