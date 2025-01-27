class Solution:
    def climbStairs(self, n: int) -> int:
        
        print("check here", int(1==1))
        
        arr = [-1] * n

        def dfs(i):

            if i >= n:
                return int(i==n)

            if arr[i] != -1:
                return arr[i]

            arr[i] = dfs(i+1) + dfs(i+2)

            return arr[i]

        return dfs(0)
        
