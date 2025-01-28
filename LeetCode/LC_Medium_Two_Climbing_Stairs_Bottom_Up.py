class Solution:
    def climbStairs(self, n: int) -> int:
        print(f"\nStarting climbStairs with n = {n}")
        
        if n <= 2:
            print(f"n <= 2, returning n directly: {n}")
            return n
            
        # Initialize dp array
        dp = [0] * (n + 1)
        dp[1], dp[2] = 1, 2
        print(f"Initialized dp array: {dp}")
        print(f"Set base cases: dp[1] = {dp[1]}, dp[2] = {dp[2]}")
        
        # Fill dp array
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
            print(f"\nStep {i}:")
            print(f"  dp[{i}] = dp[{i-1}] + dp[{i-2}]")
            print(f"  dp[{i}] = {dp[i-1]} + {dp[i-2]} = {dp[i]}")
            print(f"  Current dp array: {dp}")
        
        print(f"\nFinal result for n = {n}: {dp[n]}")
        return dp[n]

if __name__ == "__main__":
    solution = Solution()
    print(solution.climbStairs(5))