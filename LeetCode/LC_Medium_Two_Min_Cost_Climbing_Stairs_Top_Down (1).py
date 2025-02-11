class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        memo = [-1] * len(cost)

        def dfs(n):
            
            if n >= len(cost):
                return 0

            if memo[n] != -1:
                return memo[n]

            first = dfs(n+1)
            second = dfs(n+2)

            result = cost[n] + min(first,second)
            memo[n] = result

            return memo[n]

        zeroStep = dfs(0)
        firstStep = dfs(1)

        print("check memo", memo)

        finalResult = min(zeroStep, firstStep)

        return finalResult
        