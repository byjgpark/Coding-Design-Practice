from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = [-1] * len(cost)
        
        
        def dfs(i):
            print(f"Entering dfs({i})")
            if i >= len(cost):
                print(f"  i={i} is beyond the array length, returning 0")
                return 0
            if memo[i] != -1:
                print(f"  Found memo[{i}] = {memo[i]}, returning it")
                return memo[i]
            print(f"  Computing cost at index {i}")
            # Recursive calls to the next two steps
            step1 = dfs(i + 1)
            print(f"  After dfs({i+1}), step1 result: {step1}")
            step2 = dfs(i + 2)
            print(f"  After dfs({i+2}), step2 result: {step2}")
            current_cost = cost[i] + min(step1, step2)
            print(f"  memo[{i}] = cost[{i}] + min({step1}, {step2}) = {current_cost}")
            memo[i] = current_cost
            return current_cost
        
        firstResult = dfs(0)
        secondResult = dfs(1)
        result = min(firstResult, secondResult)
        print("Final memo array:", memo)
        return result
    
if __name__ == "__main__":
    sol = Solution()
    print("Test case 1: [10, 15, 20]")
    print("Result:", sol.minCostClimbingStairs([10, 15, 20]))
    # Uncomment the next lines to test the second case
    # print("\nTest case 2: [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]")
    # print("Result:", sol.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))