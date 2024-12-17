from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        print("Initial dictionary:", h)
        
        # First loop: Populate the dictionary
        for i in range(len(nums)):
            h[nums[i]] = i
            print(f"After processing nums[{i}] = {nums[i]}: {h}")
        
        print("\nStarting second loop...\n")
        
        # Second loop: Find the two numbers
        for i in range(len(nums)):
            y = target - nums[i]
            print(f"Index: {i}, nums[i]: {nums[i]}, target: {target}, y: {y}, dictionary: {h}")
            
            if y in h and h[y] != i:
                print(f"Match found! nums[i]: {nums[i]}, y: {y}, i: {i}, h[y]: {h[y]}")
                # return [i, h[y]]
            else:
                print(f"No match for index {i}. Moving to the next iteration.\n")
        
        print("No solution found.")
        return []

if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    solution = Solution()
    result = solution.twoSum(nums, target)
    print("Result:", result)