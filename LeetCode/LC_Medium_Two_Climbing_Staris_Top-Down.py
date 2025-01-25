class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 1
            
        cache = [-1] * n
        print(f"Initial cache: {cache}\n")

        def dfs(i):
            print(f"Entering dfs({i})")
            
            # Base case handling
            if i >= n:
                result = 1 if i == n else 0
                print(f"  Base case: i={i} {'==' if result else '>'} n, return {result}")
                return result
                
            # Cache check
            if cache[i] != -1:
                print(f"  Cache HIT at i={i}, value={cache[i]}")
                return cache[i]
                
            print(f"  Cache MISS at i={i}, calculating dfs({i+1}) + dfs({i+2})")
            
            # Recursive calls
            left = dfs(i + 1)
            print(f"  Back in dfs({i}) after dfs({i+1}) → {left}")
            
            right = dfs(i + 2)
            print(f"  Back in dfs({i}) after dfs({i+2}) → {right}")
            
            # Store result in cache
            cache[i] = left + right
            print(f"  Storing cache[{i}] = {left} + {right} = {cache[i]}")
            print(f"  Current cache state: {cache}\n")
            return cache[i]

        result = dfs(0)
        print(f"\nFinal cache state: {cache}")
        return result

if __name__ == "__main__":
    n = 3
    print(f"Number of ways to climb {n} stairs: {Solution().climbStairs(n)}")