class Solution:
    def climbStairs(self, n: int) -> int:
        
        def dfs(i):
            if i >= n:
                return i == n
            return dfs(i + 1) + dfs(i + 2)
            
        return dfs(0)

if __name__ == "__main__":
    n = 3
    print(f"Number of ways to climb {n} stairs: {Solution().climbStairs(n)}")