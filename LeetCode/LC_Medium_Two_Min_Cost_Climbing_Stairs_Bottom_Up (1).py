class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        dp = (len(cost) +1) * [0]

        print("dp = ", dp)
        print("cost = ", cost)

        for i in range(2, len(dp)):

            dp[i] = min( cost[i-2] + dp[i-2], cost[i-1] + dp[i-1])

            # return dp[i]
        
        print("check array of dp =", dp)

        return dp[len(dp)-1]

