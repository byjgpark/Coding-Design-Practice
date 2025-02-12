from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n + 1)
        
        
        # Debug: initial state
        print("Initial dp:", dp)
        print("Cost array:", cost)
        
        for i in range(2, n + 1):
            option1 = dp[i - 1] + cost[i - 1]  # Taking one step from i-1
            option2 = dp[i - 2] + cost[i - 2]  # Taking two steps from i-2
            dp[i] = min(option1, option2)
            
            # Debug: Print the computation details for current iteration
            print(f"\ni = {i}")
            print(f"Option1: dp[{i - 1}] ({dp[i - 1]}) + cost[{i - 1}] ({cost[i - 1]}) = {option1}")
            print(f"Option2: dp[{i - 2}] ({dp[i - 2]}) + cost[{i - 2}] ({cost[i - 2]}) = {option2}")
            print(f"Chosen dp[{i}] = {dp[i]}")
            print("Current dp state:", dp)
        
        # Debug: Final state
        print("\nFinal dp array:", dp)
        return dp[n]
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.minCostClimbingStairs([10, 15, 20]))

